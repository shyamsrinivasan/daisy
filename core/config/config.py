import os
from dotenv import load_dotenv
from os import getenv


load_dotenv()

class CoreConfig():
    ENVIRONMENT = getenv('ENVIRONMENT')
    DATABASE_URL = getenv('DATABASE_URL')
    MODEL_GEN_FILE = getenv('MODEL_GEN_FILE')
    SECRET_KEY = getenv('SECRET_KEY')
    ALGORITHM = getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
    DEFAULT_USER_PASSWORD = getenv('DEFAULT_USER_PASSWORD')
    BASE_TEMPLATE_DIR = getenv('BASE_TEMPLATE_DIR')
    BASE_DIR = os.getcwd()
    # TEMPLATE_DIR = os.path.join(BASE_DIR, BASE_TEMPLATE_DIR)
    WKHTMLTOPDF_PATH = getenv('WKHTMLTOPDF_PATH')


class RedisConfig():
    REDIS_HOST = getenv("REDIS_HOST")
    REDIS_PORT = int(getenv("REDIS_PORT")) if getenv("REDIS_PORT") else 0
    REDIS_USER = getenv("shyamsrinivasan")
    REDIS_PASS = getenv("serendipity")
    