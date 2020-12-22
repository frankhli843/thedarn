import pytest
from thedarn.argument_parser import Parser
from thedarn.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['thedarn'], _args()),
    (['thedarn', '-a'], _args(alias='darn')),
    (['thedarn', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='darn', enable_experimental_instant_mode=True)),
    (['thedarn', '-a', 'fix'], _args(alias='fix')),
    (['thedarn', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['thedarn', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['thedarn', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['thedarn', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['thedarn', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['thedarn', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['thedarn', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['thedarn', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
