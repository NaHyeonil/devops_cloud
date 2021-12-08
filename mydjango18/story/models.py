from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Storyboard(Timestamp):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "창작 이야기"
        verbose_name_plural = "이야기 목록"


class Comment(Timestamp):
    post = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "이야기 댓글"
        verbose_name_plural = "댓글 목록"


class Tag(Timestamp):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
