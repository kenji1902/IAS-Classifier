# Generated by Django 4.1 on 2022-10-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_authentication_educationalattainment'),
    ]

    operations = [
        migrations.AddField(
            model_name='authentication',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]