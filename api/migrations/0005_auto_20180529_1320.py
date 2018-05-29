# Generated by Django 2.0.5 on 2018-05-29 09:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180529_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adv_to_show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Advertisement'),
        ),
        migrations.AlterField(
            model_name='typedwords',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 29, 13, 20, 0, 896400)),
        ),
    ]