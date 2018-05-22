# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-17 14:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.IntegerField(choices=[(0, 'Llegada tarde'), (1, 'Retiro anticipado')])),
                ('justified', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField()),
                ('percentage', models.FloatField(choices=[(0.25, '1/4'), (0.5, '1/2'), (0.75, '3/4'), (1.0, '1')])),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_tel', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('student_tag', models.IntegerField()),
                ('list_number', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'REGULAR'), ('2', 'PRIMERA REINCORPORACION'), ('3', 'SEGUNDA REINCORPORACION'), ('4', 'LIBRE')], max_length=1)),
                ('food_obvs', models.CharField(max_length=50)),
                ('preceptor', models.ManyToManyField(to='controlAsistencia.Preceptor')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_number', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto'), (6, 'Sexto'), (7, 'Septimo')])),
                ('division', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (3, 'C')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Year'),
        ),
        migrations.AddField(
            model_name='preceptor',
            name='year',
            field=models.ManyToManyField(to='controlAsistencia.Year'),
        ),
        migrations.AddField(
            model_name='parent',
            name='childs',
            field=models.ManyToManyField(to='controlAsistencia.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='absence',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlAsistencia.Student'),
        ),
    ]
