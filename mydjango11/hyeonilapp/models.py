from django.db import models

class hyeonil(models.Model):
    gamename = models.CharField(max_length=100, verbose_name="게임명")
    gamedate = models.DateField(verbose_name="플레이 날짜")
    clear = models.BooleanField(verbose_name="클리어 여부")
    gold = models.CharField(max_length=100, verbose_name="획득골드")