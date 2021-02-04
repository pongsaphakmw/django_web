from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Examscore ,AllStudent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Homepage(request):
	# return HttpResponse('<h1>Hello Tester</h1>')
	return render(request, 'school/home.html')

def Aboutpage(request):
	return render(request, 'school/Aboutpage.html')

def ContactUs(request):
	return render(request, 'school/Contact.html')
@login_required
def ShowScore(request):
	score = Examscore.objects.all()

	context = {'score':score}

	return render(request, 'school/showscore.html', context)

def Register(request):

	if request.method == 'POST' :
		data = request.POST.copy()
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)
		newuser.save()
		return redirect('home-page')

	return render(request, 'school/register.html')

@login_required
def Search (request):
	##Models.object.all() ดึงค่าทั้งหมด modelsคือชื่อ
	# search = AllStudent.object.get(student_id = '')
	return render(request, 'school/search.html')





