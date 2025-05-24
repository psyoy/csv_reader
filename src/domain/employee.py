from dataclasses import dataclass

@dataclass
class Employee:
    department: str
    name: str
    email: str
    rate: int
    hours: int
    payout: str
