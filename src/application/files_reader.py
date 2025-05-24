from abc import ABC, abstractmethod

from src.domain.employee import Employee
from src.domain.table import Table


class FilesReader(ABC):
    report_name: str

    @abstractmethod
    def _read(self, file_path: str) -> None:
        pass

    @abstractmethod
    def process_files(self) -> None:
        pass

    @abstractmethod
    def get_report_name(self) -> str:
        pass

    @abstractmethod
    def get_employees(self) -> list[Employee]:
        pass