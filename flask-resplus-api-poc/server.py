#!/usr/bin/env python

from flask import Flask
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)

name_space = api.namespace('api', description='flask-resplus-api-poc APIs')


def main():
    print('API')
    app.run(debug=True)


@name_space.route("/")
class MainClass(Resource):
    def get(self):
        return {
            "status": "Got new data"
        }

    def post(self):
        return {
            "status": "Posted new data"
        }


if __name__ == '__main__':
    main()
