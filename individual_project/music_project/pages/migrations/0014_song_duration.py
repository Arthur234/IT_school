# Generated by Django 2.2.1 on 2019-06-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20190609_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
