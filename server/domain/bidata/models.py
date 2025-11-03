from django.db import models
from domain.blog.models import User

class BIData(models.Model):
    author = models.ForeignKey(User, related_name="bidatas", on_delete=models.CASCADE)
    type = models.TextField(verbose_name="类型",null=True,blank=True        )
    memo = models.TextField(verbose_name="备注",null=True,blank=True)
    content = models.TextField(verbose_name="内容")