# Generated by Django 5.0 on 2023-12-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loventoutou", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="breeding_name",
            field=models.CharField(default=None, max_length=70, verbose_name="elevage"),
        ),
        migrations.AlterField(
            model_name="dog",
            name="name",
            field=models.CharField(max_length=50, verbose_name="nom"),
        ),
        migrations.AlterField(
            model_name="owner",
            name="first_name",
            field=models.CharField(max_length=50, verbose_name="prénom"),
        ),
        migrations.AlterField(
            model_name="owner",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="nom"),
        ),
    ]
