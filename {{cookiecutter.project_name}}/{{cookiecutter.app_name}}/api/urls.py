from {{cookiecutter.app_name}}.api.health_identify import HealthIdentify
from {{cookiecutter.app_name}}.api import api
from {{cookiecutter.app_name}}.api.views import HelloView


api.add_url_rule(
    "/health", view_func=HealthIdentify.as_view(name="health"), methods=["GET"]
)

api.add_url_rule(
    "/", view_func=HelloView.as_view(name="hello"), methods=["GET"]
)
