# Generated by Django 4.1.2 on 2022-10-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_imagemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
