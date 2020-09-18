import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv('DBHOST')
NAME = os.getenv('DBNAME')
USER = os.getenv('DBUSER')
PASSWORD = os.getenv('DBPASSWORD')