import argparse

from src.application.args_parser_usecase import ArgsParserUseCase


def test_args_parser():
    pars = ArgsParserUseCase()
    args = pars.get_args()
    assert isinstance(args, argparse.Namespace)
    assert hasattr(args, 'files')
    assert hasattr(args, 'report')

if __name__ == '__main__':
    test_args_parser()

