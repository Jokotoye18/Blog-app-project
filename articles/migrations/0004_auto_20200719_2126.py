# Generated by Django 3.0.7 on 2020-07-19 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200711_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_added']},
        ),
    ]