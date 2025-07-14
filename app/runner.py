from app.commands.run_tests import RunTestsCommand
from app.commands.deploy import DeployCommand

class WorkflowRunner:
    def run_workflow(self, nome):
        if nome == "test":
            cmd = RunTestsCommand()
        elif nome == "deploy":
            cmd = DeployCommand()
        else:
            print(f"Workflow '{nome}' não é reconhecido.")
            return
        cmd.execute()