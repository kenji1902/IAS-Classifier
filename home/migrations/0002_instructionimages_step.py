# Generated by Django 4.1 on 2022-09-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructionimages',
            name='step',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
