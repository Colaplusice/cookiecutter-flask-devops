from configs.base_config import Config


class TestConfig(Config):
    DATABASE_URL = "mysql+pool://root:newpass@mysql/{{cookiecutter.project_name}}_test"

    DEBUG = True
