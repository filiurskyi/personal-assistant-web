# Generated by Django 5.0.2 on 2024-02-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
