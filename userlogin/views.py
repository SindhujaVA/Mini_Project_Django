from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
from django.contrib.sessions.models import Session

# Create your views here.
class UserAuth(APIView):
	def post(self,request):
		username = request.data.get("username")
		password = request.data.get("password")
		if User.objects.filter(username=username).exists():
			user=list(User.objects.values())
			request.session['a']=user
			print(request.session.get('a'))
			print("username exists")
			return Response({"status":True})
		else:
			print("username does not exists")
			firstname = request.data.get("firstname")
			lastname = request.data.get("lastname")
			username = request.data.get("username")
			password = request.data.get("password")
			email = request.data.get("email")
			mobileno = request.data.get("mobileno")
			User.objects.create(firstname=firstname, lastname=lastname, username=username, password=password, emailid=email, mobileno=mobileno)
			user=list(User.objects.values())
			request.session['a']=user
			print(request.session.get('a'))
			return Response("True")
			
		if not User.objects.filter(password=password).exists():
		    print("Incorrect password, please enter the correct password")
		return Response("True")


def login(request):
    return render(request,'form/login.html')

def register(request):
    return render(request,'form/register.html')

def profile(request):
	users=request.session.get('a')
	return render(request,'form/profile.html',{"users1":users})

