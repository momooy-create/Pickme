from django.shortcuts import render
from .models import Women

def Womenhome(request):
	women = Women.objects
	return render(request, 'Women.html', {'Women':women})

