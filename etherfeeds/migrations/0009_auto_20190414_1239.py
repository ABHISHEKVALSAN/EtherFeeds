# Generated by Django 2.1.3 on 2019-04-14 12:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0008_auto_20190412_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('time_exp_days', models.IntegerField(default=0)),
                ('time_exp_hours', models.IntegerField(default=0)),
                ('time_exp_minutes', models.IntegerField(default=0)),
                ('hashAnsEnt', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
                ('result', models.IntegerField(default=1)),
                ('exp_time', models.DateTimeField(default=datetime.datetime(2019, 4, 24, 12, 38, 59, 584536), verbose_name='date expiring')),
                ('hashMemProp', models.CharField(max_length=200)),
                ('proposer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='etherfeeds.Users')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='hashAns',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='answerentries',
            name='hashAnsEnt',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='finalAns',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 12, 38, 59, 583296), verbose_name='date expiring'),
        ),
    ]
