# Generated by Django 3.1 on 2020-08-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_account_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
