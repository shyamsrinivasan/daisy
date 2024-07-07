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
    ACCESS_TOKEN_EXPIRE_MINUTES = getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    DEFAULT_USER_PASSWORD = getenv('DEFAULT_USER_PASSWORD')
    BASE_TEMPLATE_DIR = getenv('BASE_TEMPLATE_DIR')
    BASE_DIR = os.getcwd()
    # TEMPLATE_DIR = os.path.join(BASE_DIR, BASE_TEMPLATE_DIR)
    WKHTMLTOPDF_PATH = getenv('WKHTMLTOPDF_PATH')