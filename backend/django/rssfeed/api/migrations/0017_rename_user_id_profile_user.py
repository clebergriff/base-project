# Generated by Django 3.2.9 on 2022-10-15 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_rename_user_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]