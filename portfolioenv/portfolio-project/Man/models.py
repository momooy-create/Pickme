from django.db import models

class Man(models.Model):
	image = models.ImageField(upload_to='images/')
	name = models.CharField(null = True, max_length=20)
