from django.shortcuts import render
from .models import Man

def Manhome(request):
	man = Man.objects
	return render(request, 'Man.html', {'Man':man})

def Mregister(request):
	return render(request, 'Mregister.html')

def man1(request):
	man1 = Man.objects
	return render(request, 'man1.html', {'man1':man1})

def man2(request):
	man2 = Man.objects
	return render(request, 'man2.html', {'man2':man2})

def man3(request):
	man3 = Man.objects
	return render(request, 'man3.html', {'man3':man3})

def man4(request):
	man4 = Man.objects
	return render(request, 'man4.html', {'man4':man4})

def man5(request):
	man5 = Man.objects
	return render(request, 'man5.html', {'man5':man5})

def man6(request):
	man6 = Man.objects
	return render(request, 'man6.html', {'man6':man6})

def man7(request):
	man7 = Man.objects
	return render(request, 'man7.html', {'man7':man7})

def man8(request):
	man8 = Man.objects
	return render(request, 'man8.html', {'man8':man8})


