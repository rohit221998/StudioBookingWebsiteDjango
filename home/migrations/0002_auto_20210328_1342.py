# Generated by Django 3.1.5 on 2021-03-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
