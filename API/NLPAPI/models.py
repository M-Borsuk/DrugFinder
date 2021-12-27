from django.db import models

# Create your models here.

class TextModel(models.Model):

    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ICD(models.Model):

    code = models.CharField(max_length=10)
    name = models.TextField()

    def __str__(self):
        return self.code
