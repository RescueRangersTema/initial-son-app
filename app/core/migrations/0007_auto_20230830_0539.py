# Generated by Django 3.2.20 on 2023-08-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230822_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='excercise',
            name='title',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='excercise',
            name='solution',
            field=models.TextField(default=None, null=True),
        ),
    ]
