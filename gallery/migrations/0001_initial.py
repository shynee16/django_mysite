# Generated by Django 2.0.6 on 2018-08-12 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.CharField(max_length=1000)),
                ('caption', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album')),
            ],
        ),
    ]
