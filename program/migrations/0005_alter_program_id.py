# Generated by Django 4.1.5 on 2023-05-30 13:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_rename_capacity_program_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
