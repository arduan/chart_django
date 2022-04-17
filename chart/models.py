import datetime
import time

from django.db import models


class GDP(models.Model):
    date = models.DateField(default=datetime.date.today())
    average = models.FloatField()


