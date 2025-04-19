import jdatetime
from django.db import models

class JalaliDateField(models.Field):
    description = "A field to store dates in the Jalali calendar"

    def db_type(self, connection):
        return 'date'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return jdatetime.date.fromgregorian(date=value)

    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, jdatetime.date):
            return value.togregorian()
        return jdatetime.date.fromisoformat(value).togregorian()

    def to_python(self, value):
        if isinstance(value, jdatetime.date):
            return value
        if value is None:
            return value
        return jdatetime.date.fromisoformat(value)
        