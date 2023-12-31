# Generated by Django 3.2.20 on 2023-10-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_excercise_is_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excercise',
            name='is_sample',
            field=models.BooleanField(default=False, help_text='Use this excercise as sample exercise in the article. Will be shown in the text.'),
        ),
    ]
