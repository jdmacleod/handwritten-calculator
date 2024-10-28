"""Provide access to Flask logger."""

from flask import current_app
from werkzeug.local import LocalProxy

# https://stackoverflow.com/questions/16994174/in-flask-how-to-access-app-logger-within-blueprint
logger = LocalProxy(lambda: current_app.logger)
