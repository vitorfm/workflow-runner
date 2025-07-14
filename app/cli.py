import click
from app.commands.runner import WorkflowRunner

@click.group()
def cli():
    pass

@cli.command()
@click.argument("nome")
def run(nome):
    """Executa um workflow com nome"""
    runner = WorkflowRunner()
    runner.run_workflow(nome)

if __name__ == "__main__":
    cli()