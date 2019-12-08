from django.shortcuts import render

def Manhome(request):
	return render(request, 'home.html')
