from django.db import models

class Women(models.Model):
	image = models.ImageField(upload_to="images/")
	이름 = models.CharField(null = True, max_length=20)
	나이 =  models.CharField(null = True, max_length=10)
	지역 = models.CharField(null = True, max_length=30)
	분야 = models.CharField(null = True, max_length=20)
	SNS = models.CharField(null = True, max_length=30)	
