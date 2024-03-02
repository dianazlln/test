from django.contrib.auth import get_user_model
from django.db import models


class Main(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)
