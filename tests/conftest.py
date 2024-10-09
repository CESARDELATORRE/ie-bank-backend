import pytest
import sys
import os

# Set environment variables
os.environ['PYTHONPATH'] = '${workspaceFolder}'
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_DEBUG'] = '1'
os.environ['FLASK_RUN_PORT'] = '5000'
os.environ['ENV'] = 'local'
os.environ['DBUSER'] = ''
os.environ['DBPASS'] = ''
os.environ['DBHOST'] = ''
os.environ['DBNAME'] = ''

## Print the current working directory and sys.path for debugging
#print("Current working directory:", os.getcwd())
#print("sys.path before modification:", sys.path)

## Add the project directory to the sys.path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

## Print sys.path after modification
#print("sys.path after modification:", sys.path)

from iebank_api.models import Account
from iebank_api import db, app

@pytest.fixture
def testing_client(scope='module'):
    with app.app_context():
        db.create_all()
        account = Account('By Default Test Account', '€', 'U.S.')
        db.session.add(account)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()

