# Generated by Django 2.0.6 on 2018-08-21 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20180821_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]