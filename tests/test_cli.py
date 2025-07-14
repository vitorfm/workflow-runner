from unittest.mock import patch
from click.testing import CliRunner
from app.cli import cli

@patch("app.cli.WorkflowRunner")
def test_cli_runs_command(mock_runner):
    mock_instance = mock_runner.return_value
    mock_instance.run_workflow.return_value = None  

    runner = CliRunner()
    result = runner.invoke(cli, ["run", "test"])

    assert result.exit_code == 0
    mock_runner.assert_called_once()
    mock_instance.run_workflow.assert_called_with("test")  
