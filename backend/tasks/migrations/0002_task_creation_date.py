# Generated by Django 5.0.6 on 2024-06-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
