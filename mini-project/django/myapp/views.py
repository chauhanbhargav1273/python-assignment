from django.shortcuts import render,redirect
from .models import Contact,user
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
		return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			remarks=request.POST['remarks'],
			)
		msg="contact saved sucessfully"
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'contacts':contacts})

def signup(request):
	if request.method=="POST":
		try:
			user.objects.get(email=request.POST['email'])
			msg="email Alredy Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:	
				user.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					gender=request.POST['gender'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
				)
				msg="user sign up sucessfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="password & confirm password does not match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')
def login(request):
	if request.method=="POST":
		try:
			users=user.objects.get(email=request.POST['email'])
			if users.password==request.POST['password']:
				request.session['email']=users.email
				request.session['fname']=users.fname
				request.session['profile_pic']=users.profile_pic.url
				return render(request,'index.html')
			else:
				msg="icorrect password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="email not registered"
			return render(request,'login.html',{'msg':msg})	
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			users=user.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for forgot password'
			message = 'Hello '+users.fname+'your OTP for forgot password Is : '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [users.email,]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'email':users.email,'otp':otp})
		except Exception as e:
			print(e)
			msg="Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,"forgot-password.html")

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		 msg="Incorrect OTP"
		 return render(request,'otp.html',{'email':email,'otp':otp,'msg':msg})

def new_password(request):
	email=request.POST['email']
	np=request.POST['new-password']
	cnp=request.POST['cnew-password']

	if np==cnp:
		users=user.objects.get(email=email)
		users.password=np
		users.save()
		msg="update password sucessfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="new password & confirm password not match"
		return render(request,'new-password.html',{'email':email,'msg':msg})


def change_password(request):
	if request.method=="POST":
		users=user.objects.get(email=request.session['email'])
		if users.password==request.POST['old-password']:
			if request.POST['new-password']==request.POST['cnew-password']:
				users.password=request.POST['new-password']
				users.save()
				return redirect('logout')
			else:
				msg="new password & confirm new password does not match"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="old password does not match"
			return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')


def profile(request):
	users=user.objects.get(email=request.session['email'])
	if request.method=="POST":
		users.fname=request.POST['fname']
		users.lname=request.POST['lname']
		users.mobile=request.POST['mobile']
		users.address=request.POST['address']
		users.gender=request.POST['gender']
		try:
			users.profile_pic=request.FILES['profile_pic']
		except:
			pass
		users.save()
		request.session['profile_pic']=users.profile_pic.url
		msg="update profile sucessfully"
		return render(request,'profile.html',{'users':users,'msg':msg})
	else:
		return render(request,'profile.html',{'users':users})