# Generated by Django 4.1 on 2022-10-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0004_remove_seedlingdispersionaffectedareas_ias_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iasdata',
            name='seedlingDispersionAffectedAreas',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='seedlingDispersionAffectedAreas',
        ),
    ]