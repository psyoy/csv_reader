import argparse
from typing import override

from src.application.files_reader import FilesReader
from src.domain.employee import Employee

class ReadCSVUseCase(FilesReader):
    def __init__(self, args: argparse.Namespace) -> None:
        self._filenames: list[str] = args.files
        self.report_name: str = args.report
        self.employees: list[Employee] = []


    @override
    def _read(self, file_name: str) -> list[dict[str, str]]:
        with open(file_name, 'r') as f:
            lines: list[str] = f.read().splitlines()
            headers: list[str] = lines[0].split(',')
            data: list[dict[str, str]] = []
            for line in lines[1:]:
                values: list[str] = line.split(',')
                row: dict[str, str] = {headers[i]: values[i] for i in range(len(headers))}
                data.append(row)
        return data

    @override
    def process_files(self) -> None:

        for file_name in self._filenames:

            dataset: list[dict[str, str]] = self._read(file_name)

            for row in dataset:
                name: str = row.get('name', '')
                email: str = row.get('email', '')
                department = row.get('department', '')
                hours = int(row.get('hours_worked', 0))
                rate: int = self._get_rate(row)
                payout: str = f'${hours * rate}'

                employee = Employee(department, name, email, rate, hours, payout)

                self.employees.append(employee)


    @override
    def get_report_name(self) -> str:
        return self.report_name

    @override
    def get_employees(self) -> list[Employee]:
        return self.employees

    @staticmethod
    def _get_rate(row: dict[str, str]) -> int:
        names: set = {"hourly_rate", "rate", "salary"}
        result: int = 0
        for name in names:
            rate: int = int(row.get(name, 0))
            if rate > 0:
                result = rate
        return result
