# Generated by Django 3.2 on 2022-07-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0041_auto_20200720_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('pinterest', 'fa-pinterest'), ('dribble', 'fa-dribbble'), ('flickr', 'fa-flickr'), ('rss', 'fa-rss'), ('google-plus', 'fa-google-plus-g'), ('facebook', 'fa-facebook'), ('instagram', 'fa-instagram'), ('linkedin', 'fa-linkedin-in')], max_length=20, null=True),
        ),
    ]
