# Generated by Django 2.0.6 on 2018-08-12 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180812_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]