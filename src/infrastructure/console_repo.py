from src.application.report_creator import ReportCreator
from src.infrastructure.report_repo import ReportRepo


class ConsoleRepo(ReportRepo):
    def __init__(self, report_creator: ReportCreator) -> None:
        self._report_creator: ReportCreator = report_creator

    def save(self) -> None:
        table: list[str] = self._report_creator.create()
        for rows in table:
            print(rows)
