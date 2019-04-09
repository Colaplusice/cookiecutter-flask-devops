from configs.base_config import Config


class ProductionConfig(Config):
    DATABASE_URL = "mysql+pool://{{cookiecutter.database_username}}:{{cookiecutter.database_password}}@db/{{cookiecutter.project_name}}"
