from app.commands.base import Command
from app.aws.lambda_client import trigger_lambda
from app.aws.s3_client import upload_to_s3
from datetime import datetime

class DeployCommand(Command):
    def execute(self):
        print("Executando etapa de deploy...")

        bucket = "workflow-runner-dev-vitor"
        timestamp = self._timestamp()
        key = f"deploys/deploy_component_{timestamp}.json"

        # Simula artefato como um log de execução de workflow
        artifact_data = {
            "workflow": "deploy_component",
            "status": "success",
            "executed_by": "DeployCommand",
            "timestamp": timestamp
        }

        print(f"Enviando artefato JSON para bucket '{bucket}'...")
        try:
            upload_to_s3(bucket, key, artifact_data)
            print("✅ Upload para o S3 realizado com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao enviar para o S3: {e}")

        print("Chamando função Lambda...")
        try:
            trigger_lambda("deploy_component")
        except Exception as e:
            print(f"❌ Erro ao chamar a Lambda: {e}")

    def _timestamp(self):
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
