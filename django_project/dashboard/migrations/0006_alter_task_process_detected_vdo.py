# Generated by Django 5.0.2 on 2024-05-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0005_task_process_extra_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task_process",
            name="detected_vdo",
            field=models.FileField(upload_to="result/"),
        ),
    ]