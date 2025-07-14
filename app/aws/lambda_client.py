import boto3
import json
from datetime import datetime

def trigger_lambda(workflow_name: str):
    client = boto3.client("lambda")

    payload = {
        "workflow": workflow_name,
        "timestamp": datetime.utcnow().isoformat(),
    }

    response = client.invoke(
        FunctionName="validate_component_deploy",  # Nome fictício
        InvocationType="RequestResponse",          # Pode ser "Event" se quiser assíncrono
        Payload=json.dumps(payload),
    )

    response_data = json.loads(response["Payload"].read())
    print("Resposta da Lambda:")
    print(json.dumps(response_data, indent=2))
