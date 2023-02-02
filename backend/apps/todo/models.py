from django.db import models


class Todo(models.Model):
    uuid = models.CharField(max_length=8, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=3000, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)
