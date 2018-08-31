import sys
from conf import settings
from server import app

# append system path
sys.path.append(settings.BASE_DIR)

# wsgi application
application = app
