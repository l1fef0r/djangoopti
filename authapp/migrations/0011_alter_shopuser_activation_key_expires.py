# Generated by Django 3.2.3 on 2021-08-07 08:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 8, 30, 41, 837089, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
