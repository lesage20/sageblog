# Generated by Django 3.0.8 on 2020-07-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200712_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('google-plus', 'fa-google-plus-g'), ('dribble', 'fa-dribbble'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('linkedin', 'fa-linkedin-in'), ('rss', 'fa-rss'), ('pinterest', 'fa-pinterest'), ('instagram', 'fa-instagram')], max_length=20, null=True),
        ),
    ]
