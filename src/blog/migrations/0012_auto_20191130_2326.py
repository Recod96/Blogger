# Generated by Django 2.2.7 on 2019-11-30 23:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191130_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 30, 23, 26, 55, 436005, tzinfo=utc)),
        ),
    ]