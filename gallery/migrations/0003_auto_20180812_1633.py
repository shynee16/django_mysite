# Generated by Django 2.0.6 on 2018-08-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180812_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
    ]