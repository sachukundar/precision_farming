# Generated by Django 3.0.8 on 2020-07-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20200727_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='values',
            name='SMS',
            field=models.IntegerField(default=170),
        ),
    ]
