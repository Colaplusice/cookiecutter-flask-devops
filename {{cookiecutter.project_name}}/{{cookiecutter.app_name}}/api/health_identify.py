from flask import request, Response
from flask.views import MethodView


class HealthIdentify(MethodView):
    def get(self):
        checktype = str(request.args.get("type"))
        if checktype in ["liveness", "readiness"]:
            return Response()
        else:
            return Response(status=404)
