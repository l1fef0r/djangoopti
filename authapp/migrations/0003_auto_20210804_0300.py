# Generated by Django 2.0 on 2021-08-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210804_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
