from flask import Flask
from flask_restful import Api,Resources,reqparse
app = Flask(__name__)
api = Api(app)