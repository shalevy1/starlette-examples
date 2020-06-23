"""Settings

Starlette project settings
"""
from starlette.config import Config

# load config from .env file
config = Config('.env')

# expose our settings in this module for use in the application
DEBUG = config.get('DEBUG', cast=bool, default=False)
SECRET = config.get('SECRET', cast=str, default='')
