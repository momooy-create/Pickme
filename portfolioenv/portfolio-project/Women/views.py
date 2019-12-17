from django.shortcuts import render
from .models import Women

def Womenhome(request):
	women = Women.objects
	return render(request, 'Women.html', {'Women':women})

def women1(request):
	women1 = Women.objects
	return render(request, 'women1.html', {'women1':women1})

def women2(request):
	women2 = Women.objects
	return render(request, 'women2.html', {'women2':women2})

def women3(request):
	women3 = Women.objects
	return render(request, 'women3.html', {'women3':women3})

def women4(request):
	women4 = Women.objects
	return render(request, 'women4.html', {'women4':women4})

def women5(request):
	women5 = Women.objects
	return render(request, 'women5.html', {'women5':women5})

def women6(request):
	women6 = Women.objects
	return render(request, 'women6.html', {'women6':women6})

def women7(request):
	women7 = Women.objects
	return render(request, 'women7.html', {'women7':women7})

def women8(request):
	women8 = Women.objects
	return render(request, 'women8.html', {'women8':women8})
