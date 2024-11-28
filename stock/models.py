from django.db import models
from accounts.models import StockUser
# ログイン中のユーザーを取得するフィールド
from django_currentuser.db.models import CurrentUserField

class Category(models.Model):
    category = models.CharField(
        verbose_name='カテゴリー',
        max_length=15
    )
    
    def __str__(self) :
        return self.category
    
# https://qiita.com/startours777/items/2a4e70ec85cc3e93a1ab
class Stocker(models.Model):
    user = models.ForeignKey(
        StockUser,
        verbose_name='ユーザ',
        on_delete= models.CASCADE
    )

    product = models.CharField(
        verbose_name='商品名',
        max_length=20,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete= models.PROTECT,
    )

    stock_quantity = models.IntegerField(
        verbose_name='在庫数',
    )

    
    create_date = models.DateTimeField(
        verbose_name="作成日時", 
        auto_now_add=True
        )

    
    update_date = models.DateTimeField(
        verbose_name="更新日時",
        auto_now=True,
        )