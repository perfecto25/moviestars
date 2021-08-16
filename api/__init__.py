from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from loguru import logger
from config import BASEDIR, LOGDIR, LOGFILE, ORIGINS

# configure logging
LOGDIR = BASEDIR + "/" + LOGDIR
if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)
logger.add(
    LOGDIR + "/" + LOGFILE,
    rotation="25MB",
    colorize=True,
    format="<green>{time:YYYYMMDD_HH:mm:ss}</green> | {level} | <level>{message}</level>",
    level="ERROR",
)

app = FastAPI()

origins = []
for o in ORIGINS.split(","):
    origins.append(o)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.views import main
