# Generated by Django 3.0.8 on 2020-07-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='the_slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
