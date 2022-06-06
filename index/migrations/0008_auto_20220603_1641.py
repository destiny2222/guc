# Generated by Django 2.2 on 2022-06-03 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20220603_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping_address',
            name='price',
        ),
        migrations.AddField(
            model_name='shipping_address',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bookname', to='index.Publication'),
            preserve_default=False,
        ),
    ]