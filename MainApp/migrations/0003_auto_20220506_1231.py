# Generated by Django 3.0.5 on 2022-05-06 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20220506_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza'),
        ),
    ]
