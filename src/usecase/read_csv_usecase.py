import argparse
from typing import override

from src.usecase.files_reader import FilesReader
from src.domain.table import Table

row = list[str]

class ReadCSVUseCase(FilesReader):
    def __init__(self, args: argparse.Namespace) -> None:
        self.filenames: list[str] = args.files
        self.tables: list[Table] = []
        self._read_files()

    @override
    def _read_files(self) -> None:
        for filename in self.filenames:
            with open(filename, 'r')as file:
                header: list[str] = next(file).strip().split(',')
                rows_str: list[str] = list(file)
                rows: list[row] = []
                for row_str in rows_str:
                    rows.append(row_str.strip().split(','))
                table: Table = Table(header, rows)
                self.tables.append(table)

    @override
    def get_tables(self) -> list[Table]:
        return self.tables
