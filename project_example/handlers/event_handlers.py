"""Event Handlers

Functions for application startup and shutdown
"""
from settings import DEBUG, SECRET


def startup():
    """Runs on app startup
    """
    print(
        f'starting application with DEBUG={DEBUG} and SECRET={SECRET}')


def shutdown():
    """Runs on app shutdown
    """
    print('shuttting application down')
