# Generated by Django 2.2.16 on 2020-10-29 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20201029_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='author_name',
        ),
    ]
