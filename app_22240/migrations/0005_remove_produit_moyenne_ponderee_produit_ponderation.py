# Generated by Django 5.0 on 2024-01-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_22240", "0004_produit_moyenne_ponderee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produit",
            name="moyenne_ponderee",
        ),
        migrations.AddField(
            model_name="produit",
            name="ponderation",
            field=models.FloatField(default=0.0),
        ),
    ]