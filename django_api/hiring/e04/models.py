from django.db import models
from django.db.models import URLField
from django.utils.timezone import now

class Company(models.Model):
    # 定義公司狀態的選項
    class CompanyStatus(models.TextChoices):
        LAYOFFS = 'layoffs'
        HIRING_FREEZE = 'hiring freeze'
        HIRING = 'hiring'

    # 公司名稱，最長 30 個字符，並設為唯一
    name = models.CharField(max_length=30, unique=True)

    # 公司狀態，選項限定為 CompanyStatus 中定義的選項
    status = models.CharField(
        max_length=30,
        choices=CompanyStatus.choices,
        default=CompanyStatus.HIRING
    )

    # 最後更新時間，默認為當前時間
    last_update = models.DateTimeField(default=now, editable=True)

    # 應用鏈接，可為空
    application_link = models.URLField(blank=True)

    # 備註，可為空
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"
