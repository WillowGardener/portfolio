# Generated by Django 3.1.7 on 2021-03-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub_app', '0004_auto_20210316_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
