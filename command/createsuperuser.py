from base import BaseCommand
import sys
from db.interface import insert_user
from werkzeug.security import generate_password_hash
from mongoengine.errors import NotUniqueError


class Command(BaseCommand):

    help = "create superuser"

    def get_version(self):
        return "v1.0.0"

    def add_parser(self, parser):
        return parser

    def handle(self, *args, **options):
        username = input("Please input username:\t")
        password = input("Please input password:\t")
        if len(username) < 6:
            sys.stderr.write("Failure, username length more than 6 letters!\n\r")

        if len(password) < 6:
            sys.stderr.write("Failure, username length more than 6 letters!\n\r")
        password_hash = generate_password_hash(password)
        try:
            insert_user(
                username=username,
                password=password_hash,
                is_superuser=True,
                is_staff=True
            )
            sys.stdout.write("Success, enjoy it!")
        except NotUniqueError as e:
            sys.stderr.write("Failure, username has already exists!\n\r")
