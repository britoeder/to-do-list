# Generated by Django 2.2.7 on 2019-11-30 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_use'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='use',
            new_name='user',
        ),
    ]
