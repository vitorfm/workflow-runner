from app.commands.base import Command

class DeployCommand(Command):
    def execute(self):
        print("Executando etapa de deploy...")
        print("Simulando envio do artefato para S3...")
        print("Deploy concluído com sucesso.")
