# Generated by Django 4.2.3 on 2023-07-14 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_usermodel_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
    ]