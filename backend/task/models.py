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

    def __str__(self):
        return self.title

class SubTask(BaseModel):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='main_task')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
