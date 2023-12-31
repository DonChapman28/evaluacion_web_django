# Generated by Django 4.2.1 on 2023-07-06 20:35

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('dv', models.CharField(max_length=1)),
                ('fecha_Nacimiento', models.DateField()),
                ('region', models.IntegerField(choices=[[0, 'Región de Arica y Parinacota'], [1, 'Región de Tarapacá'], [2, 'Región de Antofagasta'], [3, 'Región de Atacama'], [4, 'Región de Coquimbo'], [5, 'Región de Valparaíso'], [6, 'Región Metropolitana'], [7, "Región de O'Higgins"]])),
                ('telefono', models.CharField(max_length=15)),
                ('nivel_Educacion', models.IntegerField(choices=[[0, 'Magister'], [1, 'Doctor'], [2, 'Profesional'], [3, 'Otro']])),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tienda_user',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
