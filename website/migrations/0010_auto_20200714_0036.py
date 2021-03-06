# Generated by Django 3.0.8 on 2020-07-14 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200713_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('instagram', 'fa-instagram'), ('dribble', 'fa-dribbble'), ('pinterest', 'fa-pinterest'), ('flickr', 'fa-flickr'), ('rss', 'fa-rss'), ('facebook', 'fa-facebook'), ('google-plus', 'fa-google-plus-g'), ('linkedin', 'fa-linkedin-in')], max_length=20, null=True),
        ),
    ]
