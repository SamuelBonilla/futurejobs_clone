"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request, Response
from flask_restplus import Resource

from flask import Blueprint, current_app
from flask_restplus import Api
from flask import current_app as app

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)


@api_rest.route('/job_post')
class Job(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self):
        #print(dir(Response))
        job_post = app.config['MODEL']['job_post']
        rows = job_post.query.all()
        data = []
        for row in rows:
            date = ''
            if row.created_date:
                date = str(row.created_date).split(" ")[0]
            _format = {"id": row.id, "title": row.title, "description": row.description, 
                       "company_name": row.company_name, "company_url": row.company_url,
                       "created_date": date}
            data.append(_format)
        return data, 200

    def post(self):
        json_payload = request.json
        title = json_payload.get('title')
        description = json_payload.get('description')
        company_name = json_payload.get('company_name')
        company_url = json_payload.get('company_url')
        if title and description and company_name and company_url:
            db = app.config['DB']
            job_post = app.config['MODEL']['job_post']
            try:
                job = job_post(title=title, description=description, company_name=company_name, company_url=company_url)
                db.session.add(job)
                db.session.commit()
            except Exception as e:
                print(e)
                return {'error': "Failed to add job"}, 500

            return {'message': 'Job created'}, 200
        return {'error': 'title, description, company_name, company_url are required'}, 500

    def put(self):
        json_payload = request.json
        id = json_payload.get('id')
        title = json_payload.get('title')
        description = json_payload.get('description')
        company_name = json_payload.get('company_name')
        company_url = json_payload.get('company_url')
        if id and title and description and company_name and company_url:
            try:
                db = app.config['DB']
                job_post = app.config['MODEL']['job_post']
                job = job_post.query.filter_by(id=id).first()
                job.title = title
                job.description = description
                job.company_name = company_name
                job.company_url = company_url
                db.session.commit()
            except Exception as e:
                print(e)
                return {'error': "Couldn't update job"}, 500
            
            return {'message': 'job update success'}
        return {'error': 'id, title, description, company_name, company_url are required'}, 500

    def delete(self):
        json_payload = request.json
        # print("------------")
        # print(json_payload)
        id = json_payload.get('id')
        if not id:
            return {'error': "id is required"}, 500

        db = app.config['DB']
        job_post = app.config['MODEL']['job_post']
        job = job_post.query.filter_by(id=id).first()
        if not job:
            return {'error': 'id dos not exist'}, 500
        db.session.delete(job)
        db.session.commit()
        return {'menssage': 'job deleted'}
