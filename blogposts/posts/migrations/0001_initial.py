# Generated by Django 4.2.3 on 2023-07-12 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticsBlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imgs')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('time_it_takes_to_read', models.CharField(max_length=20)),
            ],
        ),
    ]
