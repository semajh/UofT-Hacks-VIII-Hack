# Generated by Django 3.1.1 on 2021-02-21 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_name', models.CharField(max_length=100)),
                ('subtopic_txt', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('topic_description', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_text', models.CharField(max_length=255)),
                ('vote_agree', models.IntegerField(default=0)),
                ('vote_unsure', models.IntegerField(default=0)),
                ('vote_disagree', models.IntegerField(default=0)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forums.subtopic')),
            ],
        ),
        migrations.AddField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forums.topic'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=255)),
                ('vote_agree', models.IntegerField(default=0)),
                ('vote_unsure', models.IntegerField(default=0)),
                ('vote_disagree', models.IntegerField(default=0)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forums.subtopic')),
            ],
        ),
    ]
