# Generated by Django 4.1.2 on 2022-11-10 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_task_deadline_alter_task_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 3, 21, 33, 288972, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='late',
            field=models.CharField(default='On Time', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 22, 21, 33, 287973, tzinfo=datetime.timezone.utc)),
        ),
    ]