# Generated by Django 3.2 on 2021-04-17 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollee', '0007_enrollee_sex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graduatedinstitution',
            old_name='insitution',
            new_name='institution',
        ),
    ]
