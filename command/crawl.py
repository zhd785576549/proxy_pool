from base import BaseCommand
from pkgutil import iter_modules
import importlib
import os
from conf import settings
import sys
from argparse import Action
import threading
import time


def get_spider_module_names():
    module_path = os.path.join(settings.BASE_DIR, "spiders")
    module_names = [name for _, name, is_pkg in iter_modules([module_path])
                    if not is_pkg and not name.startswith('_')]
    return module_names


def load_module(module_name):
    module_str = 'spiders.%s' % module_name
    module = importlib.import_module(module_str)
    return module


def start_spider_module(module_name):
    module = load_module(module_name)
    spider = module.Spider()
    spider.run()


class ALlAction(Action):

    def __init__(self,
                 option_strings,
                 dest="===ALL===",
                 default="",
                 help="start all spiders"):
        super(ALlAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        module_names = get_spider_module_names()
        for module_name in module_names:
            th = threading.Thread(target=start_spider_module, args=(module_name,))
            th.daemon = True
            th.start()
        while True:
            time.sleep(1)


class ListAction(Action):
    def __init__(self,
                 option_strings,
                 dest="===LIST===",
                 default="",
                 help="show spider module list"):
        super(ListAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        self.get_list()

    def get_list(self):
        module_names = get_spider_module_names()
        sys.stdout.write("Available spider modules:\n\r")
        for module_name in module_names:
            sys.stdout.write("\t%s\n\r" % module_name)


class Command(BaseCommand):
    help = "start crawl proxy information"

    def get_version(self):
        return "v1.0.0"

    def add_parser(self, parser):
        parser.add_argument("--list", "-l", action=ListAction)
        parser.add_argument("--all", "-a", action=ALlAction)
        parser.add_argument("--target", "-t", required=False, help="execute spider module")
        return parser

    def handle(self, *args, **options):
        target = options.pop("target", None)
        spider_modules = get_spider_module_names()
        if target:
            if target in spider_modules:
                module = load_module(target)
                module.Spider().run()
            else:
                sys.stdout.write("%s is not available module\n\r" % target)
                sys.stdout.write("available spider module:\n\r")
                for module_name in spider_modules:
                    sys.stdout.write("\t%s\n\r" % module_name)
