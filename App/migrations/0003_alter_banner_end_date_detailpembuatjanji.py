# Generated by Django 5.0.6 on 2024-06-28 04:08

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_article_created_at_alter_article_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 5, 11, 8, 17, 539469)),
        ),
        migrations.CreateModel(
            name='DetailPembuatJanji',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('perusahaan', models.CharField(max_length=225, verbose_name='Nama Perusahaan')),
                ('alamat_perusahaan', models.CharField(max_length=225, verbose_name='Alamat Perusahaan')),
                ('email_perusahaan', models.CharField(max_length=225, verbose_name='Email Perusahaan')),
                ('nomor_perusahaan', models.CharField(max_length=225, verbose_name='Nomor Perusahaan')),
                ('web_perusahaan', models.CharField(max_length=225, verbose_name='Web Perusahaan')),
                ('meeting', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=225)),
                ('alamat_meeting', models.CharField(max_length=225, verbose_name='Alamat Meeting')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='admin')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]