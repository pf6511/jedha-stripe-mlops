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

- **Feature Store offline** : données analytiques utilisées notamment pour la constitution des datasets ML ;
- **Feature Store online** : features accessibles pour les traitements de prédiction.

Dans le prototype de la plateforme :

- **Snowflake** est utilisé pour le Feature Store offline ;
- **MongoDB** fournit une représentation des features destinée aux usages online.

## 🤖 Training et Prediction

Les composants de training permettent de construire les datasets nécessaires et d'entraîner les modèles.

Les composants de prediction prennent en charge :

- la préparation des features ;
- l'exécution des modèles ;
- la production des résultats de prédiction.

Le projet fournit notamment les pipelines associés aux modèles **fraud** et **customer**.

## 📊 Evaluation et Monitoring

Les composants d'évaluation permettent d'analyser les résultats des modèles.

La couche de monitoring fournit les éléments nécessaires au suivi des modèles déployés et à la production de données et rapports de monitoring.

## 📦 Registry et gestion des artefacts

Le projet comprend des composants dédiés à la gestion :

- des modèles ;
- des datasets ;
- des résultats d'expérimentation ;
- des artefacts associés au cycle de vie Machine Learning.

**MLflow** est notamment intégré pour la gestion et le suivi du cycle de vie des modèles.

## 🛡️ Compliance

La couche compliance permet de formaliser :

- les politiques et règles de conformité ;
- les datasets nécessaires aux contrôles ;
- les findings ;
- les rapports de conformité.

## 🔄 Orchestration

Le repository contient des **DAGs Airflow** permettant de formaliser les dépendances et l'orchestration des traitements, notamment pour :

- les pipelines ELT ;
- la construction des datasets ;
- l'entraînement ;
- le registry ;
- le déploiement ;
- le monitoring ;
- la compliance.

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