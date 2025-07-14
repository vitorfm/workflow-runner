from app.commands.run_tests import RunTestsCommand

def test_run_tests_command_runs_without_error(monkeypatch):
    # Simula o subprocess sem rodar de verdade
    def fake_run(cmd):
        print(f"Comando simulado: {cmd}")
        return 0

    monkeypatch.setattr("subprocess.run", fake_run)

    cmd = RunTestsCommand()
    cmd.execute()  # Não deve lançar erro
