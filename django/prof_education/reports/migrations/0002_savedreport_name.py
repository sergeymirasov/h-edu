# Generated by Django 3.2 on 2021-04-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedreport',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Название'),
        ),
    ]