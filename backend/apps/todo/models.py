from django.db import models
from django.utils import timezone


class TodoRecord(models.Model):
    uuid = models.CharField(max_length=8, db_index=True)
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField(max_length=3000, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)
