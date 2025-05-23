from abc import ABC, abstractmethod

from src.domain.table import Table


class FilesReader(ABC):
    @abstractmethod
    def _read_files(self) -> None:
        pass

    @abstractmethod
    def get_tables(self) -> list[Table]:
        pass
