# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('Отдел', models.CharField(max_length=255, verbose_name='Отдел')),
                ('Вместимость', models.IntegerField(verbose_name='Вместимость')),
            ],
            options={
                'verbose_name_plural': 'Комнаты',
                'verbose_name': 'Комнаты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('Имя', models.CharField(max_length=255, verbose_name='Имя')),
                ('Зарплата', models.IntegerField(verbose_name='Зарплата')),
                ('Дата поступления на работу', models.DateField(verbose_name='Дата поступления на работу')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователи',
            },
            bases=(models.Model,),
        ),
    ]
