from {{cookiecutter.app_name}}.api.health_identify import HealthIdentify
from {{cookiecutter.app_name}}.api import api

api.add_url_rule(
    "/health", view_func=HealthIdentify.as_view(name="health"), methods=["GET"]
)
