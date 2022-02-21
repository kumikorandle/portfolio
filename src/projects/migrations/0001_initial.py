# Generated by Django 4.0.2 on 2022-02-21 02:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('role', models.TextField(help_text='Describe your role in the project (e.g., front end developer)')),
                ('repo', models.URLField()),
                ('link', models.URLField(blank=True, default='')),
                ('date', models.DateField(default=datetime.date.today, help_text='Enter the date the project was completed.')),
                ('technology', models.ManyToManyField(blank=True, to='technology.Technology')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/screenshots')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project')),
            ],
        ),
    ]
