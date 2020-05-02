from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
	status = (('start','start'),
				('doing','doing'),
				('done','done'))

	task = models.CharField(max_length=100)
	status = models.CharField(max_length=100,null=True , choices = status)


	def __str__(self):
		return self.work

	def get_absolute_url(self):
		return reverse('index')