# Generated by Django 4.1.6 on 2023-02-03 19:59

import apps.todo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todorecord_delete_todo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todorecord',
            options={'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
        migrations.AlterField(
            model_name='todorecord',
            name='uuid',
            field=models.CharField(db_index=True, default=apps.todo.models.UUIDGenerator.generate_unique_uuid, max_length=8),
        ),
    ]
