from flask import jsonify
from flask.views import MethodView


class HelloView(MethodView):
    def get(self):
        return jsonify("thanks for use my cookiecutter template !")
