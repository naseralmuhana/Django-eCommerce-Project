# Generated by Django 3.0.6 on 2020-06-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200617_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Amman', max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Jordan', max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='Street ....', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='07X XXXX XXX', max_length=15),
        ),
    ]
