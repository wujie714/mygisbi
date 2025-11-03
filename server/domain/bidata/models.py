from django.db import models
from domain.blog.models import User

class BIData(models.Model):
    author = models.ForeignKey(User, related_name="bidatas", on_delete=models.CASCADE)
    content = models.TextField()