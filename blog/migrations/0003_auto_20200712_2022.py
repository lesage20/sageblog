# Generated by Django 3.0.8 on 2020-07-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_the_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='the_slug',
        ),
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
        migrations.AddField(
            model_name='video',
            name='lien',
            field=models.URLField(null=True),
        ),
    ]
