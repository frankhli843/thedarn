from thedarn.specific.apt import apt_available
from thedarn.specific.sudo import sudo_support
from thedarn.utils import for_app

enabled_by_default = apt_available


@sudo_support
@for_app('apt')
def match(command):
    return command.script == "apt list --upgradable" and len(command.output.strip().split('\n')) > 1


@sudo_support
def get_new_command(command):
    return 'apt upgrade'
