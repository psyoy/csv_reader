from dataclasses import dataclass

from src.domain.employee import Employee


@dataclass
class Table:
    name: str
    header: list[str]
    rows: list[Employee]
