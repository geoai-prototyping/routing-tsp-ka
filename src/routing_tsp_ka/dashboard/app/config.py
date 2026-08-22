# Implement the configuration of the app
from os import environ as env

class Config:
    # Database configuration
    FLASK_APP = env.get('FLASK_APP')
