# Generated by Django 2.0.1 on 2018-03-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='attraction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
