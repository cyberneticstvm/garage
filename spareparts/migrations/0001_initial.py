# Generated by Django 5.0.1 on 2024-02-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spareparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_part_name', models.CharField(blank=True, max_length=150, null=True)),
                ('cost_per_unit', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
