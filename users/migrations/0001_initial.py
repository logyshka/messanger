# Generated by Django 5.2 on 2025-04-15 23:23

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 32 characters or fewer. Letters, digits only.', max_length=32, unique=True, validators=[users.validators.UsernameValidator()], verbose_name='username')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
