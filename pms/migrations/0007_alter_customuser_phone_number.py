# Generated by Django 4.1 on 2023-10-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0006_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
