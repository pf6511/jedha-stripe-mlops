from airflow.sdk import task
from airflow.sdk import task_group

from src.ml.services.deployment_service import DeploymentService
from src.ml.config.model_definition import ModelDefinition


@task_group(group_id="deployment")
def deployment_group(model_definition: ModelDefinition):
    """
    Deploy the selected model into production.
    """

    @task
    def deploy_model():
        """
        Deploy the approved model.
        """
        DeploymentService.deploy_model(model_definition)

    @task
    def validate_deployment():
        """
        Validate deployment health.
        """
        DeploymentService.validate_deployment(model_definition)

    @task
    def notify_deployment():
        """
        Notify deployment completion.
        """
        DeploymentService.notify_deployment(model_definition)

    (
        deploy_model()
        >> validate_deployment()
        >> notify_deployment()
    )