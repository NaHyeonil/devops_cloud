# Generated by Django 3.2.9 on 2021-11-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=20, verbose_name='게임명')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='게임플레이 시작')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='게임플레이 종료')),
                ('gamedate', models.DateTimeField(verbose_name='플레이 날짜')),
                ('content', models.TextField(verbose_name='특이사항')),
                ('clear', models.BooleanField(verbose_name='클리어 여부')),
                ('gold', models.CharField(max_length=100, verbose_name='획득골드')),
            ],
        ),
    ]
