from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 50)
    info = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
