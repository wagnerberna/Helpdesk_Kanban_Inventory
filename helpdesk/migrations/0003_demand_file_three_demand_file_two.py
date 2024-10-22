# Generated by Django 4.1.5 on 2023-05-16 11:17

from django.db import migrations, models
import helpdesk.models


class Migration(migrations.Migration):
    dependencies = [
        ("helpdesk", "0002_demand_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="demand",
            name="file_three",
            field=models.FileField(
                blank=True, null=True, upload_to=helpdesk.models.Demand.file_upload
            ),
        ),
        migrations.AddField(
            model_name="demand",
            name="file_two",
            field=models.FileField(
                blank=True, null=True, upload_to=helpdesk.models.Demand.file_upload
            ),
        ),
    ]
