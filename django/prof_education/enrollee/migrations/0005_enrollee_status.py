# Generated by Django 3.2 on 2021-04-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollee', '0004_educationdoc_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollee',
            name='status',
            field=models.CharField(choices=[('enrollee', 'Абитуриент'), ('student', 'Студент'), ('rejected', 'Не поступил')], default='enrollee', max_length=8, verbose_name='Статус'),
        ),
    ]
