# Generated by Django 3.0.8 on 2020-07-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20200716_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('flickr', 'fa-flickr'), ('linkedin', 'fa-linkedin-in'), ('instagram', 'fa-instagram'), ('rss', 'fa-rss'), ('google-plus', 'fa-google-plus-g'), ('pinterest', 'fa-pinterest'), ('facebook', 'fa-facebook')], max_length=20, null=True),
        ),
    ]
