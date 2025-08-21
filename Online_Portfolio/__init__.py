from flask import Flask

app = Flask(__name__)

from . import app  # if your routes/views are in app.py

