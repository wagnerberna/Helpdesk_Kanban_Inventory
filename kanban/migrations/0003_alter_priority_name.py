# Generated by Django 4.1.5 on 2023-05-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kanban", "0002_priority_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="priority",
            name="name",
            field=models.CharField(blank=True, max_length=1, null=True, unique=True),
        ),
    ]
