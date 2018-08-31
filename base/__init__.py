from lxml import etree
from argparse import ArgumentParser
import os


class BaseSpider(object):

    name = ""

    def run(self):
        self.start()

    def start(self):
        raise NotImplementedError("This method must be provided.")

    def get_selector(self, content):
        html = etree.HTML(content)
        return html


class BaseCommand(object):

    help = ''  # help message

    def get_version(self):
        """
        Get version

        :return [str]:
            command version
        """
        return "v1.0.0"

    def _run(self, *args, **options):
        """
        Inner run

        :param prog_name[str]: program name
        :param script_name[str]: script name base on Command
        :param options[dict]: options
        """
        self.handle(*args, **options)

    def handle(self, *args, **options):
        """
        Impletement method handle[abstract]

        :param prog_name[str]: program name
        :param script_name[str]: script name base on Command
        :param options[dict]: options
        """
        raise NotImplementedError('Handle method must be provided')

    def create_parser(self, prog_name, script_name):
        """
        Create Parser

        :param prog_name[str]: program name
        :param script_name[str]: script name base on Command

        :return [ArgumentParser]:
            argument parser object
        """
        parser = ArgumentParser(
            prog='%s %s' % (os.path.basename(prog_name), script_name)
        )
        parser.add_argument('--version', action='version', version=self.get_version())
        return parser

    def add_parser(self, parser):
        """
        Add params parser

        :param parser[ArgumentParser]: argument parser object

        :return [ArgumentParser]:
            argument parser object after add new arguments
        """
        raise NotImplementedError('add_parser must be provided')

    def run_from_argv(self, argv):
        """
        Run from argvs

        Parser from system arguments (sys.argv), and parser from the third arg

        :param argv[list]: arguments from system
        """

        parser = self.create_parser(argv[0], argv[1])
        parser = self.add_parser(parser)

        # start parser arguments from the third position
        options = parser.parse_args(argv[2:])
        cmd_options = vars(options)
        args = cmd_options.pop('args', ())
        self._run(*args, **cmd_options)
