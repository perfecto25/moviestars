import os
import sys
from dotenv import load_dotenv
from os.path import join, dirname

BASEDIR = os.getcwd()
LOGDIR = "logs"
LOGFILE = "moviestar.log"
BIND = "0.0.0.0"


if len(sys.argv) < 2:
    print("no env provided from Pipfile")
    sys.exit(1)

dotenv_path = join(dirname(__file__), f".env.{sys.argv[1]}")
load_dotenv(dotenv_path)

PORT = os.environ.get("PORT")
WORKERS = os.environ.get("WORKERS")
RELOAD = os.environ.get("RELOAD")
ORIGINS = os.environ.get("ORIGINS")
NB_ENV = os.environ.get("NB_ENV")