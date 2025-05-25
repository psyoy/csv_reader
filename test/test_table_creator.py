from src.application.create_table_usecase import CreateTableUseCase
from unittest.mock import MagicMock


def test_table_creation():
    mock_reader = MagicMock()
    mock_reader.get_employees.return_value = []
    mock_reader.get_report_name.return_value = 'payout'

    table_creator = CreateTableUseCase(mock_reader)
    table = table_creator.create_table()

    assert table.name == 'payout'
    assert table.header == ['department', 'name', 'email', 'hours', 'payout']