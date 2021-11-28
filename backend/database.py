from app import app
from flaskext.mysql import MySQL
import json
import os

mysql = MySQL()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'config.json'), 'r') as j:
    data_dict = json.loads(j.read())
app.config['MYSQL_DATABASE_USER'] = data_dict["USER"]
app.config['MYSQL_DATABASE_PASSWORD'] = data_dict["PASSWORD"]
app.config['MYSQL_DATABASE_DB'] = data_dict["DB"]
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
