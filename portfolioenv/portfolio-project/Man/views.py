from django.shortcuts import render
from .models import Man

def Manhome(request):
	man = Man.objects
	return render(request, 'Man.html', {'Man':man})
