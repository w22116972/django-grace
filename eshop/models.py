from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分類名稱')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分類'
        verbose_name_plural = '分類'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='標籤名稱')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class PhoneCase(models.Model):
    name = models.CharField(max_length=255, verbose_name='手機殼名稱')
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='內容'
    )
    original_price = models.PositiveIntegerField(default=0, verbose_name='原價')
    sell_price = models.PositiveSmallIntegerField(default=0, verbose_name='售價')

    STATUS_CHOICES = (
        (0, '未上架'),
        (1, '上架中'),
        (2, '已上架')
    ) 
    
    status = models.PositiveSmallIntegerField(
        verbose_name='狀態',
        choices=STATUS_CHOICES,
        default=0
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='新增時間')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新時間')
    # published = models.DateTimeField(null=True)
    seller = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='賣家名稱'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
         return self.name

    class Meta:
        verbose_name = '手機殼'
        verbose_name_plural = '手機殼'


