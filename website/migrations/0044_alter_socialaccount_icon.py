# Generated by Django 3.2 on 2022-07-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0043_alter_socialaccount_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('flickr', 'fa-flickr'), ('facebook', 'fa-facebook'), ('instagram', 'fa-instagram'), ('google-plus', 'fa-google-plus-g'), ('pinterest', 'fa-pinterest'), ('linkedin', 'fa-linkedin-in'), ('rss', 'fa-rss')], max_length=20, null=True),
        ),
    ]
