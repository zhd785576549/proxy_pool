from pkgutil import iter_modules
import os
import importlib
import sys


def get_script_names():
    """
    Given a path to a management directory, return a list of all the script
    names

    :return [list]:
        all available script names
    """
    command_module_path = os.path.abspath(os.path.dirname(__file__))
    script_modules = [ name for _, name, is_pkg in iter_modules([command_module_path])
                       if not is_pkg and not name.startswith('_') ]
    return script_modules


def load_class(script_name):
    """
    Load script class from module

    :param script_name: [str] script name

    :return [cls]:
        Script class base on Command class, must be named Command
    """
    module_str = 'command.%s' % script_name
    module = importlib.import_module(module_str)
    return module.Command


def print_help(commands, prog_name, sub_command):
    """
    Print help content
    :param commands:
    :param prog_name:
    :param sub_command:
    :return:
    """
    if sub_command:
        sys.stderr.write('%s is not command\n\r' % sub_command)
    sys.stdout.write('available command: \n\r')
    for name in commands:
        c = load_class(name)
        sys.stdout.write('\t%s\t\t%s\r\n' % (name, c.help))
    sys.stdout.write('\n\r')
    sys.stdout.write('command help use %s [command] -h\n\r' % prog_name)


def run_command_from_argv(argv):
    """
    Run command from argv

    :param argv: [str] system argvs
    """
    prog_name = argv[0]
    commands = get_script_names()
    try:
        sub_command = argv[1]
        if sub_command not in commands:
            print_help(commands, prog_name, sub_command)
            return

        c = load_class(sub_command)
        c_i = c()
        c_i.run_from_argv(argv)
    except IndexError as e:
        print_help(commands, prog_name, None)

