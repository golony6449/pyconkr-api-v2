# Generated by Django 4.1.5 on 2023-05-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_program'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='capacity',
            new_name='slot',
        ),
    ]
