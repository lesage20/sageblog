# Generated by Django 3.0.8 on 2020-07-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200714_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('rss', 'fa-rss'), ('linkedin', 'fa-linkedin-in'), ('pinterest', 'fa-pinterest'), ('google-plus', 'fa-google-plus-g'), ('facebook', 'fa-facebook'), ('instagram', 'fa-instagram'), ('flickr', 'fa-flickr')], max_length=20, null=True),
        ),
    ]
