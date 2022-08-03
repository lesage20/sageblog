# Generated by Django 3.2 on 2022-07-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0046_alter_socialaccount_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('instagram', 'fa-instagram'), ('linkedin', 'fa-linkedin-in'), ('dribble', 'fa-dribbble'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('google-plus', 'fa-google-plus-g'), ('rss', 'fa-rss'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]