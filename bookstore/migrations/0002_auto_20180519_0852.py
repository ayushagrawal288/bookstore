# Generated by Django 2.0.5 on 2018-05-19 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='data_published',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
