# Generated by Django 5.0.6 on 2024-05-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=6),
        ),
    ]