# Generated by Django 5.2.3 on 2025-06-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableau',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
    ]
