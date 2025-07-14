# workflow-runner

![CI](https://github.com/vitorfm/workflow-runner/actions/workflows/ci.yml/badge.svg)


Projeto didático para simular a execução de workflows automatizados com Python, aplicando:

- APIs RESTful com FastAPI
- CLI com Click
- Execução de tarefas com subprocess e padrões de projeto (Command + Repository)
- Integração com AWS (Lambda)
- Testes com pytest
- CI/CD com GitHub Actions

## Rodando a API

```bash
uvicorn app.main:app --reload

## ☁️ Integração com AWS Lambda

Este projeto integra a execução de workflows locais com a AWS via Lambda, utilizando a biblioteca `boto3`.

---

### 📌 Comando `deploy`

O comando `deploy` simula o envio de um componente e chama uma função Lambda real na AWS.

```bash
python -m app.cli run deploy

