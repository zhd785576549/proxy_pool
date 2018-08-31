from base import BaseCommand


class Command(BaseCommand):

    help = "run cron schedule"

    def get_version(self):
        return "v1.0.0"

    def add_parser(self, parser):
        return parser

    def handle(self, *args, **options):
        pass
