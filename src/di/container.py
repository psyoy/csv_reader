import argparse

from src.application.create_payout_report_usecase import CreatePayoutReportUseCase
from src.application.create_table_usecase import CreateTableUseCase
from src.application.report_creator import ReportCreator
from src.application.table_creator import TableCreator
from src.infrastructure.report_repo import ReportRepo
from src.infrastructure.console_repo import ConsoleRepo
from src.application.args_parser_usecase import ArgsParserUseCase
from src.application.files_reader import FilesReader
from src.application.read_csv_usecase import ReadCSVUseCase


class Container:
    def __init__(self):
        self.args_parser_service: ArgsParserUseCase = ArgsParserUseCase()
        self.args: argparse.Namespace = self.args_parser_service.get_args()
        self.file_reader: FilesReader = ReadCSVUseCase(self.args)
        self.file_reader.process_files()
        self.table_creator: TableCreator = CreateTableUseCase(self.file_reader)
        self.report_creator: ReportCreator = CreatePayoutReportUseCase(self.table_creator)
        self.report_repo: ReportRepo = ConsoleRepo(self.report_creator)


    def create(self) -> None:
        self.report_repo.save()
