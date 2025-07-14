import subprocess
from  app.commands.base import Command

class RunTestsCommand(Command):
    def execute(self):
        print("Executando testes com pytest...")
        subprocess.run(["pytest"])