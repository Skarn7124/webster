# Generated by Django 4.1.2 on 2022-11-10 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_task_late'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='task',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 20, 22, 41, 237620, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 1, 22, 41, 237620, tzinfo=datetime.timezone.utc)),
        ),
    ]
