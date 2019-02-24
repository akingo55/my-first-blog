from django.db import models
from django.utils import timezone

#モデルを定義する
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #他のモデルへのリンク
    title = models.CharField(max_length=200) #文字数が制限されたテキストを定義するフィールド
    text = models.TextField() #制限無しの長いテキスト用
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title