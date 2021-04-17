# Generated by Django 3.2 on 2021-04-16 21:15

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.educationorg', verbose_name='Учебная организация')),
            ],
            options={
                'verbose_name': 'Член приемной комиссии',
                'verbose_name_plural': 'Члены приемной комиссии',
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]