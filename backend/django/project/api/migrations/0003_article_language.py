# Generated by Django 3.2.9 on 2022-09-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_article_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
