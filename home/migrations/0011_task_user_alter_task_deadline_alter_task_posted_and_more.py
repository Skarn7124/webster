# Generated by Django 4.1.2 on 2022-11-11 02:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_task_completion_alter_task_deadline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 7, 38, 1, 832107, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 11, 2, 38, 1, 832107, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]