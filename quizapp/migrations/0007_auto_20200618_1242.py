# Generated by Django 3.0.7 on 2020-06-18 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_auto_20200618_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertracker',
            name='quiztakers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.QuizTakers'),
        ),
    ]
