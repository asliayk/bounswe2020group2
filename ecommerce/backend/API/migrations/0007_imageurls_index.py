# Generated by Django 3.1.3 on 2020-12-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20201210_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageurls',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]