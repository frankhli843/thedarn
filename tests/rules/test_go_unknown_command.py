import pytest
from thedarn.rules.go_unknown_command import match, get_new_command
from thedarn.types import Command
from thedarn.utils import which


@pytest.fixture
def build_misspelled_output():
    return '''go bulid: unknown command
Run 'go help' for usage.'''


def test_match(build_misspelled_output):
    assert match(Command('go bulid', build_misspelled_output))


def test_not_match():
    assert not match(Command('go run', 'go run: no go files listed'))


@pytest.mark.skipif(not which('go'), reason='Skip if go executable not found')
def test_get_new_command(build_misspelled_output):
    assert get_new_command(Command('go bulid', build_misspelled_output)) == 'go build'
