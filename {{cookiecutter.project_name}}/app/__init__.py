from coast.flask.app import BaseApp


class App(BaseApp):
    def batch_register_blueprint(self):
        pass

    def ready(self):
        {%- if cookiecutter.create_api == 'y'%}
        from .api import api as api_blueprint

        self.register_blueprint(api_blueprint, url_prefix="/{{cookiecutter.project_name}}")
        {%- endif %}
