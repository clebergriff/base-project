# Generated by Django 4.1.2 on 2022-10-15 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_image_alter_profile_thumbnail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageModel',
        ),
    ]