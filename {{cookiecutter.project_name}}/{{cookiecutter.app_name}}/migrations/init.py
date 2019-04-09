from {{cookiecutter.app_name}}.extentions import db


def migrate_up():
    print("run successful!")
    db.database.create_tables([])


def rollback():
    pass
