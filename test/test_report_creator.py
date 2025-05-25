from unittest.mock import MagicMock
from src.application.create_payout_report_usecase import CreatePayoutReportUseCase
from src.application.table_creator import TableCreator
from src.domain.table import Table, Employee


def test_report_creation():
    employees = [Employee('IT', 'John', 'j@j.com', 20, 10, '$200')]
    table = Table('payout', ['dept', 'name', 'email', 'hrs', 'rate', 'payout'], employees)

    mock_creator = MagicMock(spec=TableCreator)
    mock_creator.create_table.return_value = table

    report_creator = CreatePayoutReportUseCase(mock_creator)
    report = report_creator.create()

    assert len(report) == 2
    assert 'John' in report[1]

if __name__ == '__main__':
    test_report_creation()