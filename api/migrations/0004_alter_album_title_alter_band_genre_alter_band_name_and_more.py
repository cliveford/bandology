# Generated by Django 4.1 on 2022-08-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_instrument_musician_instrument_musician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musician',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='musician',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
