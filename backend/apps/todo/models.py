import uuid
from django.db import models
from django.utils import timezone


class UUIDGenerator:
    @staticmethod
    def generate_unique_uuid(length=8):
        """
        Generates unique uuid for the TodoRecord.

        :param model: The model for which the uuid should be generated.
        :param length: Length of the generated uuid (default is 8).
        :return: The generated unique uuid.
        """
        def _generate_uuid():
            """
            Helper function to generate the uuid.
            """
            return str(uuid.uuid4())[:length]

        new_uuid = _generate_uuid()
        if TodoRecord.objects.filter(uuid=new_uuid).exists():
            return UUIDGenerator.generate_unique_uuid(length)
        return new_uuid


class TodoRecord(models.Model):
    uuid = models.CharField(
        max_length=8,
        db_index=True,
        default=UUIDGenerator.generate_unique_uuid
    )
    created = models.DateTimeField(
        default=timezone.now
    )
    body = models.TextField(
        max_length=3000,
        blank=False,
        null=False
    )
    active = models.BooleanField(
        default=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
