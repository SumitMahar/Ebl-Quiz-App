# Generated by Django 4.0 on 2021-12-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('no_of_questions', models.IntegerField()),
                ('duration', models.IntegerField(help_text='Duration of the Quiz in minutes')),
                ('req_score_to_pass', models.IntegerField(help_text='Required score in %')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
