from django.db import models
from django.utils.timezone import now
# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=200)