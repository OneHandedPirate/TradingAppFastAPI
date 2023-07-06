import os
from dotenv import load_dotenv


load_dotenv()

SK = os.getenv('SK')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DB = os.getenv('DB_DB')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


DB_USER_TEST = os.getenv('DB_USER_TEST')
DB_PASSWORD_TEST = os.getenv('DB_PASSWORD_TEST')
DB_DB_TEST = os.getenv('DB_DB_TEST')
DB_HOST_TEST = os.getenv('DB_HOST_TEST')
DB_PORT_TEST = os.getenv('DB_PORT_TEST')


REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
