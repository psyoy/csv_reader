from abc import ABC, abstractmethod

from src.domain.table import Table


class TableCreator(ABC):
    header: str

    @abstractmethod
    def create_table(self)-> Table:
        pass