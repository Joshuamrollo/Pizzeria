# Generated by Django 3.0.5 on 2022-05-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
