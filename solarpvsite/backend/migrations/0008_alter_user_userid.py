# Generated by Django 3.2.9 on 2021-11-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20200430_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]