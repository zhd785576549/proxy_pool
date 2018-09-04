import sys
from conf import settings
from server.api import app
from db import init_db

# append system path
sys.path.append(settings.BASE_DIR)


# init db
init_db()

# wsgi application
application = app
