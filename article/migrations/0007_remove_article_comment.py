# Generated by Django 2.2.1 on 2019-05-10 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
    ]
