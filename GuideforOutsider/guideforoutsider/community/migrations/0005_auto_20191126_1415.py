# Generated by Django 2.1.1 on 2019-11-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20191126_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='time_table',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
