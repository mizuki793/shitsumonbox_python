# api/__init__.py

from flask import Flask

app = Flask(__name__)
app.config.from_object('api.config')

import api.views
