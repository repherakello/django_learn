from django.db import models
from users.models import user
# Create your models here.
class upload(models.model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    content = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(user, on_delete=models.CASCADE)
    thumbnail = models.URLField()
