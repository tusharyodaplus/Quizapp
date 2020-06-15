# Generated by Django 3.0.7 on 2020-06-15 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_quiz_quiztakers'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizapp.Quiz'),
            preserve_default=False,
        ),
    ]