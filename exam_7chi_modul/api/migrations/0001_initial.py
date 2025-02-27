# Generated by Django 5.1 on 2024-08-18 12:22

import api.helpers
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=4)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_business_image)),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=4)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='api_busines_id_221d53_idx')],
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_clients_image)),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=4)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='api_clients_id_610565_idx')],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_services_image)),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=4)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='api_service_id_a4070a_idx')],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=4)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.services')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_users_image)),
                ('level', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('status', models.CharField(choices=[('df', 'Draft'), ('pb', 'Publish')], default='pb', max_length=5)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
                'indexes': [models.Index(fields=['id'], name='api_users_id_2cd2f9_idx')],
            },
        ),
    ]
