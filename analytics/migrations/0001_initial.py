# Generated by Django 4.1 on 2022-10-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plantreports',
            fields=[
                ('date', models.DateField(auto_now=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('chartdata', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]