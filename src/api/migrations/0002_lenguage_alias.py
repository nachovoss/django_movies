# Generated by Django 3.2.17 on 2023-02-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lenguage',
            name='alias',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
