# Generated by Django 3.2.9 on 2022-09-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_article_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(default='en', max_length=200),
        ),
    ]