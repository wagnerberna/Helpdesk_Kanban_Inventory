# Generated by Django 4.1.5 on 2023-05-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "inventory",
            "0005_switchmanufacturer_switchmodel_switchhardware_switch_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="switch",
            name="password",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="switch",
            name="user",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
