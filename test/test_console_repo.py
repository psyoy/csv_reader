from src.infrastructure.console_repo import ConsoleRepo
from unittest.mock import MagicMock


def test_console_output(capsys):
    mock_report = ["Header", "Row1"]
    mock_creator =  MagicMock()
    mock_creator.create.return_value = mock_report

    repo = ConsoleRepo(mock_creator)
    repo.save()

    captured = capsys.readouterr()
    assert "Header\nRow1" in captured.out  # [[5]]