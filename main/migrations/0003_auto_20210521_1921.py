# Generated by Django 2.2.12 on 2021-05-21 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210518_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='signupDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 21, 19, 21, 18, 640554)),
        ),
    ]
