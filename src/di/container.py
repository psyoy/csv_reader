import argparse

from src.data.report_repo import ReportRepo
from src.data.console_repo import ConsoleRepo
from src.usecase.args_parser_usecase import ArgsParserUseCase
from src.usecase.files_reader import FilesReader
from src.usecase.read_csv_usecase import ReadCSVUseCase


class Container:
    def __init__(self):
        self.args_parser_service: ArgsParserUseCase = ArgsParserUseCase()
        self.args: argparse.Namespace = self.args_parser_service.get_args()
        self.file_reader: FilesReader = ReadCSVUseCase(self.args)
        self.report_repo: ReportRepo = ConsoleRepo(self.file_reader.get_tables())


    def create(self) -> None:
        self.report_repo.save()
