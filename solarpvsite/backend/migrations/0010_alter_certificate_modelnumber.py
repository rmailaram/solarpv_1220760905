# Generated by Django 3.2.9 on 2021-11-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_location_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='modelnumber',
            field=models.CharField(max_length=200),
        ),
    ]