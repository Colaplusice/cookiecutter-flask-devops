from {{cookiecutter.app_name}}.api import api
from {{cookiecutter.app_name}}.api.views import HelloView


api.add_url_rule(
    "/", view_func=HelloView.as_view(name="hello"), methods=["GET"]
)
