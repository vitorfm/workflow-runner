class WorkflowRepository:
    def __init__(self):
        self._workflows = []

    def add(self, nome: str):
        self._workflows.append(nome)

    def list_all(self):
        return self._workflows