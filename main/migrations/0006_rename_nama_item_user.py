# Generated by Django 4.2.5 on 2023-09-26 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_item_nama'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='nama',
            new_name='user',
        ),
    ]