# Generated by Django 4.2.2 on 2023-10-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('megaApp', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cid',
            new_name='hid',
        ),
    ]
