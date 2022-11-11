# Generated by Django 4.1.2 on 2022-11-11 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_task_deadline_alter_task_late_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion',
            field=models.CharField(default='Not done', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 7, 14, 5, 557621, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 2, 14, 5, 557621, tzinfo=datetime.timezone.utc)),
        ),
    ]
