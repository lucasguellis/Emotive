# Generated by Django 4.2.3 on 2024-01-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_weatherdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='air_quality',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
