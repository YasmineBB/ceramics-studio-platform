# Generated by Django 3.2.15 on 2022-10-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_platform', '0006_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=200),
        ),
    ]
