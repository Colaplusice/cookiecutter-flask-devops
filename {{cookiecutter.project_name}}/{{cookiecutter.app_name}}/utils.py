import datetime

import peewee
import pendulum
from flask import render_template


def not_exist(error):
    return render_template("errors/404.html")


class DatetimeTZField(peewee.Field):
    field_type = "DATETIME"

    def python_value(self, value):
        if isinstance(value, str):
            return pendulum.parse(value)
        if isinstance(value, datetime.datetime):
            return pendulum.instance(value)
        return value

    def db_value(self, value):
        if value is None:
            return value
        if not isinstance(value, datetime.datetime):
            raise ValueError("datetime instance required")
        if value.utcoffset() is None:
            raise ValueError("timezone aware datetime required")
        if isinstance(value, pendulum.DateTime):
            value = datetime.datetime.fromtimestamp(
                value.timestamp(), tz=value.timezone
            )
        return value.astimezone(datetime.timezone.utc)
