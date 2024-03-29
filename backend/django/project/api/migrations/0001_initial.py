# Generated by Django 3.2.9 on 2022-09-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('thumbnail', models.URLField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
