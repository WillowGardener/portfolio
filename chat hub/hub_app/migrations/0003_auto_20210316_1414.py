# Generated by Django 3.1.7 on 2021-03-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub_app', '0002_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(default=None),
        ),
    ]