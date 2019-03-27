from configs.base_config import Config


class DevConfig(Config):
    DEBUG = True
    DATABASE_URL = "mysql://root:newpass@localhost/{{cookiecutter.project_name}}"
