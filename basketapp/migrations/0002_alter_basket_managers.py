# Generated by Django 3.2.3 on 2021-08-11 12:22

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='basket',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
