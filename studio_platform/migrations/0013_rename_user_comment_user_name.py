# Generated by Django 3.2.15 on 2022-11-09 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio_platform', '0012_alter_userprofile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_name',
        ),
    ]
