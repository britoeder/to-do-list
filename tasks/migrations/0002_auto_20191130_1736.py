# Generated by Django 2.2.7 on 2019-11-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Fazendo'), ('done', 'Feito')], max_length=5),
        ),
    ]
