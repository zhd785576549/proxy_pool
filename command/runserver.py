from base import BaseCommand
from server import start_api_server


class Command(BaseCommand):

    help = "start api http server"

    def get_version(self):
        return "v1.0.0"

    def add_parser(self, parser):
        parser.add_argument("addrport", nargs="?", default="localhost:8000", help="start server by ip:port")
        return parser

    def handle(self, *args, **options):
        addport = options.pop("addrport", None)
        if addport:
            ip, port = addport.split(":")
            start_api_server(ip, port)
