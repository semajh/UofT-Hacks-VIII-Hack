# Generated by Django 3.1.1 on 2021-02-21 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtopic',
            name='subtopic_txt',
        ),
    ]
