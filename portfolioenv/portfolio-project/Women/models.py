from django.db import models

class Women(models.Model):
	image = models.ImageField(upload_to="images/")
	name = models.CharField(null = True, max_length=20)
	title =  models.CharField(null = True, max_length=200)
	pub_date = models.DateTimeField(null = True)
	body = models.TextField(null = True)

