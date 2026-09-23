from __future__ import annotations

import mlflow

from src.ml.catalog.model_catalog import ModelCatalog
from src.ml.config.model_definition import ModelDefinition

from src.ml.training.training_dataset import TrainingDatasetSnapshot

from src.ml.training.trainer import Trainer
from src.ml.evaluation.evaluator import Evaluator

from src.ml.experiment.experiment_result import ExperimentResult

from src.ml.models.mlflow_prediction_model import MLflowPredictionModel
from src.ml.infrastructure.mlflow_pyfunc_model import MLflowPyFuncModel

from src.ml.training.training_model import TrainingModel

class TrainingService:
    """
    Application service orchestrating a complete ML training pipeline.
    """

    _catalog = ModelCatalog()
    _trainer = Trainer()
    _evaluator = Evaluator()

    @staticmethod
    def train_model(
        training_dataset: TrainingDatasetSnapshot,
        model_definition: ModelDefinition,
    ) -> ExperimentResult:
        """
        Execute a complete MLflow training run.
        """

        #
        # Resolve model components.
        #
        model_feature_components = TrainingService._catalog.get(
            model_definition,
        )

        #
        # Execute the MLflow experiment.
        #
        with mlflow.start_run() as run:

            #
            # Train the model.
            #
            training_model: TrainingModel = model_definition.estimator_class(
                **model_definition.estimator_params,
            )

            training = TrainingService._trainer.train(
                model=training_model,
                training_dataset=training_dataset.dataset,
            )
            #
            # Evaluate the trained model.
            #
            evaluation = TrainingService._evaluator.evaluate(
                training,
            )

            #
            # Log evaluation metrics.
            #
            mlflow.log_metrics(
                evaluation.metrics,
            )

            # Build the application-level prediction model.
            prediction_model = MLflowPredictionModel(
                estimator=training.estimator,
                model_feature_components=model_feature_components,
            )

            # Wrap the prediction model for MLflow PyFunc.
            pyfunc_model = MLflowPyFuncModel(
                prediction_model=prediction_model,
            )

            #
            # Log the prediction model.
            #
            mlflow.pyfunc.log_model(
                name="model",
                python_model=pyfunc_model,
            )

            return ExperimentResult(
                run_id=run.info.run_id,
                model_uri=f"runs:/{run.info.run_id}/model",
            )