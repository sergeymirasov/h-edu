# Generated by Django 3.2 on 2021-04-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollee', '0003_auto_20210417_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdoc',
            name='grade',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Оценка'),
            preserve_default=False,
        ),
    ]
