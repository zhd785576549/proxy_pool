from command import run_command_from_argv
from db import init_db
import sys


if __name__ == "__main__":
    init_db()
    run_command_from_argv(sys.argv)
