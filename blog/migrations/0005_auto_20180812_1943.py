# Generated by Django 2.0.6 on 2018-08-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_seo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='seo_url',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]