from django.db import models

# Create your models here.

import json
from django.db import models

class Config(models.Model):

    type = models.CharField("配置分类", max_length=128)
    name = models.CharField("配置名称", max_length=128)
    value = models.CharField("配置值", max_length=256)
    des = models.CharField("描述", max_length=256, blank=True, null=True)
    class Meta:
        db_table = "config"
        verbose_name = '配置中心'
        verbose_name_plural = verbose_name