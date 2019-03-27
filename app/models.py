from app import app, db
import datetime
from sqlalchemy.dialects.postgresql import JSON


class JobPost(db.Model):
    __tablename__ = 'job_post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Text)
    company_name = db.Column(db.String())
    company_url = db.Column(db.String())
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, description, company_name, company_url):
        self.title = title
        self.description = description
        self.company_name = company_name
        self.company_url = company_url

    def __repr__(self):
        return '<id {}>'.format(self.id)