# Generated by Django 3.1.5 on 2021-01-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210114_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='join_date',
            field=models.DateField(blank=True, verbose_name='Date'),
        ),
    ]