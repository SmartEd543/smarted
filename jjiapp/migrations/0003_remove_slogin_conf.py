# Generated by Django 5.0.7 on 2024-12-25 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0002_slogin_delete_signin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slogin',
            name='conf',
        ),
    ]