# Generated by Django 4.2.2 on 2023-09-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpHotelApp', '0004_alter_hotel_hdisc_alter_hotel_hprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img_url',
            field=models.ImageField(default=' ', upload_to='images/'),
        ),
    ]
