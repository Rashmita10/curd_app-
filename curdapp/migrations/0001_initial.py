# Generated by Django 4.0.3 on 2022-06-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('assignment1', models.IntegerField()),
                ('assignment2', models.IntegerField()),
                ('assignment3', models.IntegerField()),
                ('assignment4', models.IntegerField()),
                ('institute', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
