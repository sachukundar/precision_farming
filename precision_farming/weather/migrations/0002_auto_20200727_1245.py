# Generated by Django 3.0.8 on 2020-07-27 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Album',
            new_name='Values',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
