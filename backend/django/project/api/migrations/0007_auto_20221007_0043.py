# Generated by Django 3.2.9 on 2022-10-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.URLField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=2048),
        ),
    ]
