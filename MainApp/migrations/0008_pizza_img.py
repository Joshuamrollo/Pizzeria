# Generated by Django 3.0.5 on 2022-05-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_remove_comment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='img',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
