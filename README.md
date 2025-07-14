# workflow-runner

Projeto didático para simular a execução de workflows automatizados com Python, aplicando:

- APIs RESTful com FastAPI
- CLI com Click
- Execução de tarefas com subprocess e padrões de projeto (Command + Repository)
- Integração com AWS (Lambda mock)
- Testes com pytest
- CI/CD com GitHub Actions

## Rodando a API

```bash
uvicorn app.main:app --reload