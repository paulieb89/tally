import pytest
from click.testing import CliRunner


@pytest.fixture
def runner(tmp_path, monkeypatch):
    monkeypatch.setenv("TALLY_STORE", str(tmp_path / "tally.json"))
    return CliRunner()
