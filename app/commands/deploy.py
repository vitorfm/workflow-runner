from app.commands.base import Command
from app.aws.lambda_client import trigger_lambda

class DeployCommand(Command):
    def execute(self):
        print("Executando etapa de deploy...")
        print("Simulando envio para S3... (não implementado ainda)")
        
        print("Chamando função Lambda 'validate_component_deploy'...")
        try:
            trigger_lambda("deploy_component")
        except Exception as e:
            print(f"Erro ao chamar a Lambda: {e}")
