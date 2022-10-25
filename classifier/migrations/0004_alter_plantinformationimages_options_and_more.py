# Generated by Django 4.1 on 2022-10-23 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_plantinformation_family_plantinformation_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plantinformationimages',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='plantinformationimages',
            name='plantInformation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='classifier.plantinformation'),
        ),
    ]