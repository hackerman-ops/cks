from django.db import models

# Create your models here.

import json
from django.db import models

class Config(models.Model):

    name = models.CharField("配置名称", max_length=128)
    value = models.CharField("配置值", max_length=256)
   
    class Meta:
        db_table = "config"
        verbose_name = '工作节点配置中心'
        verbose_name_plural = verbose_name
