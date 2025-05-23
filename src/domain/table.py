from dataclasses import dataclass

row = list[str]

@dataclass
class Table:
    header: list[str]
    rows: list[row]
