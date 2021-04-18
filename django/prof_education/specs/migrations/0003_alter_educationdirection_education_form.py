# Generated by Django 3.2 on 2021-04-18 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0002_alter_educationdirection_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationdirection',
            name='education_form',
            field=models.CharField(choices=[('full_time', 'Очная'), ('part_time', 'Очно-заочная'), ('distance', 'Заочная')], db_index=True, max_length=9, verbose_name='Форма обучения'),
        ),
    ]
