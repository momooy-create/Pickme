from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == "POST" :
		if request.POST["password1"] == request.POST["password2"]:
			user = User.objects.create_user(
				username = request.POST["username"],password=request.POST["password1"])
			auth.login(request,user)
			return redirect('Main')
		return render(request, 'signup.html')
		
	return render(request, 'signup.html')

def login(request):
	if request.method == "POST" :
		username = request.POST['username'] 
		password = request.POST['password']
		user = auth.authenticate(request, username=username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('Main')  # 아이디와 비밀번호가 일치하면 로그인 성공 후 메인페이지로
		else:
			return render(request, 'login.html', {'error': '아이디 혹은 비밀번호를 확인해 주세요.'})
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'login.html')	
