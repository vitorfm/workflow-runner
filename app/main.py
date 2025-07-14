
from fastapi import FastAPI
from app.repository.workflow_repo import WorkflowRepository

app = FastAPI()
repo = WorkflowRepository()

@app.get("/workflows")
def listar_workflows():
    return repo.list_all()

@app.post("/workflows")
def registrar_workflow(nome: str):
    repo.add(nome)
    return {"message": f"Workflow '{nome}' registrado com sucesso."}
