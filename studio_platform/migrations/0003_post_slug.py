# Generated by Django 3.2.15 on 2022-10-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_platform', '0002_auto_20221004_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
