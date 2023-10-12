# Generated by Django 4.2.2 on 2023-09-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('cid', models.BigIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.CharField(max_length=35)),
                ('cpass', models.CharField(max_length=12)),
                ('cstatus', models.CharField(default='True', max_length=7)),
                ('cdt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
