# Generated by Django 3.2.17 on 2023-02-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230213_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file_url',
            field=models.URLField(max_length=255),
        ),
    ]
