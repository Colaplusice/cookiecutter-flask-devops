import os

from peewee import AutoField, CharField
from werkzeug.utils import import_string
from datetime import datetime

from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.utils import DatetimeTZField


class MigrateRecord(db.Model):
    created_at = DatetimeTZField(default=datetime.now())
    name = CharField(null=False)
    migrate_id = AutoField()


def run():
    """
    database make migrate
    integration with flask-script
    usage: python run.py migrate
    """
    if not db.database.table_exists("migraterecord"):
        db.database.create_tables([MigrateRecord])

    package_name = "jasmine_app/migrations"
    if not os.path.exists(package_name):
        os.mkdir(package_name)
    file_list = os.listdir(package_name)
    migration_list = []
    for file in file_list:
        if not file.endswith(".py") or file == "__init__.py":
            continue
        print(file)
        import_name = package_name.replace("/", ".") + "." + file[:-3] + ":migrate_up"
        print(import_name)
        function = import_string(import_name)
        migration_list.append((file[:-3], function))
    migrate_records = {record.name for record in MigrateRecord.select()}
    for migrate in migration_list:
        if migrate[0] not in migrate_records:
            migrate[1]()
            MigrateRecord.create(**{"name": migrate[0]})


def destroy():
    pass
    # db.database.
