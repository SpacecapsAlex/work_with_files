# Generated by Django 5.0.3 on 2024-03-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('manufacturer', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='', verbose_name='car_image/')),
                ('file', models.FileField(upload_to='', verbose_name='car_file/')),
            ],
        ),
    ]
