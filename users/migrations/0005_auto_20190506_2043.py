# Generated by Django 2.2.1 on 2019-05-06 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190506_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aboutme',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=50)),
                ('school', models.CharField(blank=True, max_length=100)),
                ('profession', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('aboutme', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
