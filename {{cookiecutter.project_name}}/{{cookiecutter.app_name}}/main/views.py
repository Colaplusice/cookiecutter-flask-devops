import os

from flask import (
    Blueprint,
    current_app,
    render_template,
    url_for,
)
from {{cookiecutter.app_name}}.utils import not_exist
from jinja2.exceptions import TemplateNotFound
from .health_identify import HealthIdentify

main = Blueprint("main", __name__)
main.register_error_handler(TemplateNotFound, not_exist)
main.add_url_rule("/health", view_func=HealthIdentify.as_view(name="health"), methods=["GET"]
)


@main.route("/")
def index():
    return render_template("index.html")


@main.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(current_app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
