# Generated by Django 5.0.1 on 2024-01-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='service',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
