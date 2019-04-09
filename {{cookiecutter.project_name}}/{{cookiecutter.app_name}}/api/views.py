from flask import Response
from flask.views import MethodView


class HelloView(MethodView):
    def get(self):
        return Response("thanks for use my cookiecutter template !")
