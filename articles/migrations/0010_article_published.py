# Generated by Django 3.0.7 on 2020-08-05 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_remove_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.CharField(choices=[('P', 'Published'), ('D', 'Draft')], default='D', max_length=1),
        ),
    ]
