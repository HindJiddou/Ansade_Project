# Generated by Django 5.2.3 on 2025-07-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0003_donnees_etiquette_ligne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donnees',
            name='etiquette_ligne',
        ),
        migrations.AddField(
            model_name='tableau',
            name='etiquette_ligne',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
