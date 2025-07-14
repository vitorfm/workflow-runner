from unittest.mock import patch
from app.commands.deploy import DeployCommand

@patch("app.commands.deploy.upload_to_s3")
@patch("app.commands.deploy.trigger_lambda")
def test_deploy_command_runs_successfully(mock_lambda, mock_upload):
    cmd = DeployCommand()
    cmd.execute()

    # Verifica se upload_to_s3 foi chamado ao menos uma vez
    assert mock_upload.called
    # Verifica se trigger_lambda foi chamado com o nome correto
    mock_lambda.assert_called_with("deploy_component")
