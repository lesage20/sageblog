# Generated by Django 3.0.8 on 2020-07-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200717_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='/static/images/usericon.png', upload_to='images'),
        ),
    ]
