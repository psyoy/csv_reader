from src.application.read_csv_usecase import ReadCSVUseCase
from unittest.mock import patch, mock_open


@patch('argparse.Namespace', autospec=True)
def test_read_csv(mock_args):
    mock_args.files = ['test.csv']
    mock_args.report = 'payout'

    csv_data = "name,email,department,hours_worked,hourly_rate\nJohn,j@j.com,IT,10,20"
    with patch('builtins.open', mock_open(read_data=csv_data)):
        reader = ReadCSVUseCase(mock_args)
        reader.process_files()

        assert len(reader.employees) == 1
        assert reader.employees[0].payout == '$200'

if __name__ == '__main__':
    test_read_csv()
