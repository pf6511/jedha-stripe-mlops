from __future__ import annotations

from src.ml.config.model_definition import ModelDefinition

from src.ml.deployment.deployment_manager import DeploymentManager


class DeploymentService:
    """
    Application service responsible for deploying machine learning models.
    """

    @staticmethod
    def deploy_model(
        model_config: ModelDefinition,
    ) -> None:
        """
        Deploy the selected model.
        """

        DeploymentManager.deploy(
            model_config=model_config,
        )

    @staticmethod
    def validate_deployment(
        model_config: ModelDefinition,
    ) -> None:
        """
        Validate the deployment.
        """

        DeploymentManager.validate(
            model_config=model_config,
        )

    @staticmethod
    def notify_deployment(
        model_config: ModelDefinition,
    ) -> None:
        """
        Notify stakeholders after a successful deployment.
        """

        DeploymentManager.notify(
            model_config=model_config,
        )