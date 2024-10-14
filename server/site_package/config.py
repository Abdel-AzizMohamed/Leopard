"""Contains flask app config"""

import os


class Config:
    SECRET_KEY = os.getenv("secret")
