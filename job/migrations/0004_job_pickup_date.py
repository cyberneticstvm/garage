# Generated by Django 5.0.1 on 2024-02-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pickup_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
