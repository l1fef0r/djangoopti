# Generated by Django 3.2.3 on 2021-08-11 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 13, 12, 22, 27, 920586, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
