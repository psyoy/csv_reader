import argparse

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
        self.report_repo: ReportRepo = ConsoleRepo(self.file_reader.get_tables())


    def create(self) -> None:
        self.report_repo.save()
