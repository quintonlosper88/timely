# Generated by Django 4.2.3 on 2023-07-15 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="timesheet",
            name="enter_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
