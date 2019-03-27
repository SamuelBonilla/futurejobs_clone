"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app, db
from .models import JobPost


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    SQLALCHEMY_DATABASE_URI = 'postgres://ohxudrwqqhmurt:13874ba7ba3339a5855e5868d0e00774afbe3ef6356e6095c341647c4ce6b0d0@ec2-184-73-216-48.compute-1.amazonaws.com:5432/dd2vcmkehsh0nb
'
    DB = db
    MODEL = {
        'job_post': JobPost 
    }
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
