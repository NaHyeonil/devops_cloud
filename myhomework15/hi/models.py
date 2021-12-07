from django.db import models

class Game(models.Model):
	gamename = models.CharField(max_length=100, verbose_name="게임명")
	gamedate = models.DateField(verbose_name="플레이 날짜")
	gold = models.TextField(blank=True, verbose_name="획득골드")
	beweis = models.ImageField(blank=True)
	claer = models.BooleanField(verbose_name="클리어 여부")
	singularity = models.TextField(blank=True, verbose_name="특이사항")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)