# Generated by Django 3.0.6 on 2020-06-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200621_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
