# Generated by Django 5.0.7 on 2024-12-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('conf', models.CharField(max_length=100, null=True)),
                ('userPass', models.JSONField(max_length=200, null=True)),
            ],
        ),
    ]