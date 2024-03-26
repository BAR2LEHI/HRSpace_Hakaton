import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_DB')


DB_USER_TEST = os.environ.get('POSTGRES_USER_TEST')
DB_PASS_TEST = os.environ.get('POSTGRES_PASSWORD_TEST')
DB_HOST_TEST = os.environ.get('POSTGRES_HOST_TEST')
DB_PORT_TEST = os.environ.get('POSTGRES_PORT_TEST')
DB_NAME_TEST = os.environ.get('POSTGRES_DB_TEST')