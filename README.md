# Stripe MLOps

Projet **MLOps** d'une plateforme fintech de type Stripe.

Ce repository constitue la couche logicielle dédiée au **cycle de vie des modèles Machine Learning**, aux **features**, à l'**entraînement**, à la **prédiction**, au **monitoring**, à la **registry** et à la **compliance**.

Le projet formalise principalement les **contrats, interfaces et flux d'artefacts** entre les différents composants du système.

## 🏗️ Principaux domaines

| Domaine | Responsabilité |
|---|---|
| Features | Définition et calcul des features |
| Feature Store | Gestion des données de features offline et online |
| Training | Construction des datasets et entraînement des modèles |
| Prediction | Exécution des pipelines de prédiction |
| Evaluation | Évaluation des résultats des modèles |
| Monitoring | Suivi des modèles déployés et de leurs performances |
| Registry | Gestion des modèles et datasets enregistrés |
| Deployment | Gestion du déploiement des modèles |
| Compliance | Contrôles et rapports de conformité |

## 🔄 Features et Feature Stores

Le projet contient les composants nécessaires à la définition et au calcul des features, notamment pour les cas d'usage **fraud** et **customer**.

Les features sont exploitées dans deux contextes :

- **Feature Store offline** : données analytiques utilisées notamment pour la constitution des datasets ML
- **Feature Store online** : features accessibles pour les traitements de prédiction

Dans le prototype de la plateforme :

- **Snowflake** est utilisé pour le Feature Store offline
- **MongoDB** fournit une représentation des features destinée aux usages online

## 🤖 Training

Les composants de training permettent de construire les datasets nécessaires et d'entraîner les modèles.

Voici le processus détaillé

### Construction du dataset d’entraînement

DatasetService coordonne la constitution du Training Dataset en déléguant l'accès aux données et les opérations de persistance aux composants spécialisés. Pour commencer OfflineFeatureStore extrait un dataset en fonction de ModelDefinition, training_start, training_end (les dates qui bornent les observations) puis DataSetService créé un TrainingDatasetSnapshot encapsulant TrainingDataset et TrainingDatasetMetadata.

### Experience d’entraînement

Ensuite TrainingService prend le relais, il reçoit en entrée Le TrainingDatasetSnaphot produit précédemment ainsi que ModelDefinition et commence à exécuter une expérience Mlflow dans le contexte de laquelle s’inscrivent les étapes qui suivent. Un estimateur est instancié conformément aux métadonnées dans ModelDefinition puis l’entraînement est délégué à Trainer qui reçoit en paramètre l’estimateur et le jeu de données d’entraînement défini en amont. A l’issue de l’entraînement (fit de l’estimateur), un TrainingResult est retourné, il encapsule l’estimateur entraîné et un dataset de validation. Puis l’évaluation du modèle est déléguée à Evaluator qui va produire un EvaluationResult (avec des métriques comme accuracy_score, f1_score,…). Ces métriques sont logguées dans mlflow. Ensuite un MLflowPyFuncModel encapsule le modèle de prédiction afin de l'adapter à l'interface MLflow PyFunc, puis est enregistré comme artefact du run. Au final TrainingService retourne un ExperimentResult qui contient le run_id ainsi que l’uri du model (dans mlflow).

### Sauvegarde du modèle (métadonnées et artifact)

L'enregistrement du modèle dans le registre est assuré par le ModelRegistryService, qui délègue cette responsabilité à la classe ModelRegistry. À partir de l'ExperimentResult produit par le TrainingService, le registre invoque mlflow.register_model() afin de créer une nouvelle version du modèle dans le MLflow Model Registry. Le modèle est identifié par son URI (model_uri) et enregistré sous le nom logique défini par la ModelDefinition. MLflow retourne alors les informations relatives au modèle enregistré, notamment sa version. Ces informations sont encapsulées dans un objet RegisteredModel.
Le ModelRegistryService transmet ensuite cet objet au ModelRepository, qui assure le catalogage des métadonnées du modèle dans Snowflake, dans le catalogue des modèles du schéma MODEL_REGISTRY.MODEL_CATALOG. Le catalogue conserve notamment le nom et la version du modèle, la référence au run MLflow ainsi que les informations relatives au Feature Set et à sa version utilisés lors de l'entraînement.
Cette organisation permet de distinguer clairement trois responsabilités complémentaires : MLflow assure le stockage et la gestion du cycle de vie des artefacts et des versions de modèles, le catalogue Snowflake conserve les métadonnées nécessaires à leur traçabilité analytique, et le ModelRegistryService orchestre ces opérations.


Le projet fournit notamment les pipelines associés aux modèles **fraud** et **customer**.

## Inférence

Le service FraudPredictionService reçoit (injection de dépendances) un FraudInferencePipeline pré configuré ainsi qu’ un MongoDbRepository). La fonction predict exécute le pipeline puis sauvegarde le résultat dans le document MongoDb sur lequel s’applique le modèle.

### Préparation du pipeline
FraudInferencePipelineBuilder prépare le pipeline en lui fournissant un modèle MlflowPredictionModel préconfiguré avec le modèle Pyfunc chargé depuis Mlflow et augmenté de ModelFeatureComponents ainsi qu’un FraudFeatureService pré-configuré avec FraudRepository.

### Etapes du pipeline
La première étape de FraudInferencePipeline consiste à déléguer à FraudFeatureService la construction du contexte de features : en plus des données d’entrée (provenant du document MongoDb – collection financial_operations), le service délègue au repository le chargement des datasets nécessaires au calcul des features dérivées. Cette première étape produit un FeatureContext.

Ensuite, le modèle délègue le calcul des features au FeatureCalculator qu’il encapsule. L’ensemble des features est transmis à la méthode predict de l’estimateur du modèle qui produit un PredictionOutput. Enfin ce dernier alimente un InferenceResult qui en plus des prédictions encapsule le contexte, les features, le nom et la version du modèle utilisé.

### Préparation du nœud ml et mise à jour du document
Ensuite, le InferenceResult retourné par la pipeline d’inférence est interprété par FraudPredictionService pour produire le nœud « ml » qui sera transmis au MongoDbRepository pour être ajouté au document MongoDb cible sur lequel est appliqué la prédiction.



## 📊 Evaluation et Monitoring

Les composants d'évaluation permettent d'analyser les résultats des modèles.

La couche de monitoring fournit les éléments nécessaires au suivi des modèles déployés et à la production de données et rapports de monitoring.

### Pipeline de Monitoring
Comme pour les pipelines d’entraînement de modèles, un DAG Airflow orchestre les tâches métier dont la responsabilité revient au MonitoringService.

### Construction du jeu de données de monitoring
MonitoringService commence par déléguer au MonitoringRepository la création d’un MonitoringDataset. Celui-ci extrait du modèle de monitoring présenté ci-dessus les observations correspondant au modèle à surveiller ainsi que la période d’analyse.

### Calcul des métriques
Ensuite une implémentation de ModelMonitor reçoit  le MonitoringDataset, configure le moteur de monitoring notamment les métriques adaptées au type de modèle analysé et évalue le dataset. Les indicateurs calculés peuvent notamment inclure
-	Accuracy
-	Precision
-	Recall
-	F1-score

### Détection des dérives
Au-delà des métriques de performance, le pipeline compare les distributions observées des caractéristiques aux données de référence afin d'identifier d'éventuelles dérives.
Cette analyse permet de détecter :
•	une évolution de la distribution des données d'entrée
•	une dégradation progressive du comportement du modèle
•	des situations nécessitant une réévaluation ou un réentraînement du modèle

### Production du rapport
À l'issue de l'analyse, le moteur de monitoring produit un MonitoringReport.
Ce rapport rassemble notamment :
•	les métriques calculées
•	les indicateurs de dérive détectés
•	les alertes générées
•	les métadonnées du modèle analysé
•	Les dates de début et de fin de période


## 📦 Registry et gestion des artefacts

Le projet comprend des composants dédiés à la gestion :

- des modèles
- des datasets
- des résultats d'expérimentation
- des artefacts associés au cycle de vie Machine Learning

**MLflow** est notamment intégré pour la gestion et le suivi du cycle de vie des modèles.

## 🛡️ Compliance

La couche compliance permet de formaliser :

- les politiques et règles de conformité
- les datasets nécessaires aux contrôles
- les findings
- les rapports de conformité

## 🔄 Orchestration

Le repository contient des **DAGs Airflow** permettant de formaliser les dépendances et l'orchestration des traitements, notamment pour :

- les pipelines ELT
- la construction des datasets
- l'entraînement
- le registry
- le déploiement
- le monitoring
- la compliance

Le moteur d'exécution **Airflow n'est pas déployé dans le prototype**. Les DAGs permettent principalement de matérialiser le cadre d'orchestration et la circulation des artefacts.

## 🔗 Intégration avec le Data Pipeline

Le projet MLOps s'intègre avec les composants Data de la plateforme :

```text
PostgreSQL / MongoDB
        │
        ▼
     Airbyte
        │
        ▼
    Snowflake
        │
        ▼
       dbt
        │
        ▼
Feature Store offline
        │
        ▼
   ML Training
        │
        ▼
     MLflow
        │
        ├──► Prediction
        ├──► Monitoring
        └──► Compliance