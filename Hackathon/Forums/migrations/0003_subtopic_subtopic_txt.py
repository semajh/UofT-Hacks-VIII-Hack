# Generated by Django 3.1.1 on 2021-02-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0002_remove_subtopic_subtopic_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopic',
            name='subtopic_txt',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
