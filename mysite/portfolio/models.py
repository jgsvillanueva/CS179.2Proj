from django.db import models

class time_stamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(time_stamp):
    title = models.CharField(max_length = 140)
    content = models.TextField()
    tag = models.CharField(max_length = 140)

    def __str__(self):
        return self.title
