import argparse

class ArgsParserUseCase:
    def __init__(self) -> None:
        self.parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Parse console arguments")
        self._add_arguments()

    def _add_arguments(self) -> None:
        self.parser.add_argument(
            'files',
            nargs='+',
            help='list of entering csv-files'
        )

        self.parser.add_argument(
            '--report',
            required=True,
            help='Report type(example=payout)'
        )

    def get_args(self) -> argparse.Namespace:
        args = self.parser.parse_args()
        return args
