# ENVIRONMENT VARIABLES
from .default import *
import os
from dotenv import load_dotenv, find_dotenv # import dotenv environment loader

load_dotenv(find_dotenv()) # load environment variables from .env file

HOST = os.environ.get('HOST', HOST)
PORT_HTTP = int(os.environ.get('HTTP_PORT', PORT_HTTP))
