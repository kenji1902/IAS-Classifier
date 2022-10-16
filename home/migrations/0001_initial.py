# Generated by Django 4.1 on 2022-10-10 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instruction',
            fields=[
                ('instruction_order', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='instructionImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('image', models.TextField(default=None)),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.instruction')),
            ],
        ),
    ]
