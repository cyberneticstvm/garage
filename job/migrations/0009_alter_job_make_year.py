# Generated by Django 5.0.1 on 2024-03-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_customersparepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='make_year',
            field=models.IntegerField(blank=True),
        ),
    ]
