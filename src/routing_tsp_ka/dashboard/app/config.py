# Implement the configuration of the app
from os import environ as env


class Config:
    """"Configuration loaded into the application.

    Returns all variables used in the application from the env file.
    """
    # Database configuration
    FLASK_APP = env.get('FLASK_APP')
