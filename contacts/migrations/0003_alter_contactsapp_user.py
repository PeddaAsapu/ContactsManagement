# Generated by Django 4.0.3 on 2022-03-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contactsapp_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsapp',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]