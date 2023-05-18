from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	job = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.name}({self.id})'