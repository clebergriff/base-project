# Generated by Django 3.2.9 on 2022-10-07 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_article_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.URLField(blank=True),
        ),
    ]
