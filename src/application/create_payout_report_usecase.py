from typing import override

from src.application.report_creator import ReportCreator
from src.application.table_creator import TableCreator
from src.domain.table import Table


class CreatePayoutReportUseCase(ReportCreator):
    def __init__(self, table_creator: TableCreator):
        self._table_creator: TableCreator = table_creator


    @override
    def create(self) -> list[str]:
        report: list[str] = []
        table: Table = self._table_creator.create_table()
        if table.name ==  "payout":
            header: str = "{:<15} {:<15} {:<25} {:<15} {:<15} {:<15}".format(
        table.header[0],
            table.header[1],
            table.header[2],
            table.header[3],
            table.header[4],
            table.header[5]
            )
            report.append(header)
            for row in table.rows:
                employee: str = "{:<15} {:<15} {:<25} {:<15} {:<15} {:<15}".format(
                    row.department,
                    row.name,
                    row.email,
                    row.hours,
                    row.rate,
                    row.payout)
                report.append(employee)
        else:
            print('can only create payout reports yet')
        return report
