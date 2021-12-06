# Generated by Django 3.2.9 on 2021-12-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=100, verbose_name='게임명')),
                ('gamedate', models.DateField(verbose_name='플레이 날짜')),
                ('gold', models.TextField(blank=True, verbose_name='획득골드')),
                ('beweis', models.ImageField(blank=True, upload_to='')),
                ('claer', models.BooleanField(verbose_name='클리어 여부')),
                ('singularity', models.TextField(blank=True, verbose_name='특이사항')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
