"""feedアプリのモデル"""
from django.db import models
from django.contrib.auth.models import User

class TimeStampModel(models.Model):
    """
    作成日時と変更日時フィールドを提供する Abstract クラス
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    """
    カテゴリ情報を保持する
    """
    category_code = models.CharField(max_length=10)
    category_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


class Channel(TimeStampModel):
    """
    チャンネル情報を保持する
    """
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Episode(TimeStampModel):
    """
    エピソード情報を保持する
    """
    channel_id = models.ForeignKey(Channel, on_delete=models.PROTECT)
    episode_title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    summary = models.TextField(null=True, blank=True)
    release_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.episode_title
