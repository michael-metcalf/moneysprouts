from dotenv import load_dotenv
from flask import Flask
import os
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_CONNECTION = os.environ.get("DB_CONNECTION")
SQLALCHEMY_DATABASE = f'postgresql://{DB_CONNECTION}'

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080", "http://localhost:5000"])
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_CONNECTION}'
db = SQLAlchemy(app)

###
#
# Creating the database
#
###

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/greenhouse")
engine = create_engine(f"postgresql://{DB_CONNECTION}")
if not database_exists(engine.url):
    create_database(engine.url)

from app import routes, models