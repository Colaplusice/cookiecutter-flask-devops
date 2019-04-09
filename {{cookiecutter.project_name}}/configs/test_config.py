from configs.base_config import Config


class TestConfig(Config):
    DATABASE_URL = "mysql+pool://{{cookiecutter.database_username}}:{{cookiecutter.database_password}}@localhost/{{cookiecutter.project_name}}_test"
