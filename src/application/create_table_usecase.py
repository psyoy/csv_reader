from src.application.files_reader import FilesReader
from src.application.table_creator import TableCreator
from src.domain.employee import Employee
from src.domain.table import Table


class CreateTableUseCase(TableCreator):
    header: list[str] = ['department', 'name', 'email', 'hours', 'payout']

    def __init__(self, files_reader: FilesReader):
        self._table_name = files_reader.get_report_name()
        self._employees: list[Employee] = files_reader.get_employees()

    def create_table(self) -> Table:
        table: Table = Table(self._table_name, self.header, [])
        for employee in self._employees:
            table.rows.append(employee)
        return table
