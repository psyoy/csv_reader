from src.infrastructure.report_repo import ReportRepo
from src.domain.table import Table


class ConsoleRepo(ReportRepo):
    def __init__(self, tables: list[Table]) -> None:
        self.tables: list[Table] = tables

    def save(self) -> None:
        for table in self.tables:
            print(table)
