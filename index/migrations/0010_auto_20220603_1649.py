# Generated by Django 2.2 on 2022-06-03 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20220603_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping_address',
            old_name='phonenumber',
            new_name='phone',
        ),
    ]
