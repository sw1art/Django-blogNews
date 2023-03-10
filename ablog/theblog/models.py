from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=40, default='blogNews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    date_post = models.DateField(auto_now=date)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('main')
        # kwargs={'pk' : self.pk} args=(str(self.id))

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('main')

    
