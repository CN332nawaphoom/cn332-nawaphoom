# Generated by Django 5.0.2 on 2024-05-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_task_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_process',
            name='extra_data',
            field=models.TextField(default=[1, 2, 3]),
            preserve_default=False,
        ),
    ]