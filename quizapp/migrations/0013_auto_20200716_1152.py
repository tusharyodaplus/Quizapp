# Generated by Django 3.0.7 on 2020-07-16 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0012_auto_20200701_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertracker',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.Question'),
        ),
    ]