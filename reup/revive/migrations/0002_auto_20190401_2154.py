# Generated by Django 2.1.7 on 2019-04-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='old_id',
            field=models.IntegerField(unique=True),
        ),
    ]
