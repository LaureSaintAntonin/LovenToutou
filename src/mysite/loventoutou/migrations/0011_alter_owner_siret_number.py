# Generated by Django 5.0 on 2024-05-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loventoutou", "0010_remove_owner_id_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="siret_number",
            field=models.PositiveBigIntegerField(
                default=None, verbose_name="numéro de siret"
            ),
        ),
    ]
