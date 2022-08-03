# Generated by Django 3.2 on 2022-08-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0048_alter_socialaccount_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('linkedin', 'fa-linkedin-in'), ('rss', 'fa-rss'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('google-plus', 'fa-google-plus-g'), ('instagram', 'fa-instagram'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]