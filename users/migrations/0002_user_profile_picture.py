# Generated by Django 4.1.7 on 2023-03-08 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(null=True, upload_to='users-profile-pictures', verbose_name='Profile picture'),
        ),
    ]