__version__ = '0.1.0'

from flask import Flask
from config import Config

app = Flask(__name__)

#loading config file
app.config.from_object(Config)

from app import routes