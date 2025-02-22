# Generated by Django 5.1.5 on 2025-01-19 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=1500, verbose_name='Original URL')),
                ('shortened_url', models.CharField(max_length=200, unique=True, verbose_name='Shortened URL')),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Creation Timestamp')),
                ('expiration_timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Expiration Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Access Timestamp')),
                ('ip_address', models.CharField(blank=True, max_length=100, verbose_name='IP Address')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_logs', to='urls.url')),
            ],
        ),
    ]
