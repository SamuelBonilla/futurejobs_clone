import os
from flask import Flask, current_app, send_file
from flask_sqlalchemy import SQLAlchemy

from app.api import api_bp
from app.client import client_bp
from flask_cors import CORS

app = Flask(__name__, static_folder='../dist/static')
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models import JobPost

db.create_all()
db.session.commit()

app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

from app.config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

@app.route('/')
def index_client():
    data = JobPost.query.all()
    print(data)
    print(data)
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


