# Generated by Django 2.1.3 on 2019-04-15 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0023_auto_20190415_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 19, 5, 0, 963000), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 19, 5, 0, 964713), verbose_name='date expiring'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 19, 5, 0, 964661), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 19, 5, 0, 963369), verbose_name='date expiring'),
        ),
    ]
