from django.shortcuts import render
from .models import User,Member
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
	return render(request,'index.html')

def login(request):
	return render(request,'login.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="email already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					)
				msg="sign up sucessfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="password & confirm password does not match"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'index.html')
			else:
				msg="incorrect password"
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
		return render(request,'index.html')
	except:
		return render(request,'login.html')

def forgot_password(request):
		if request.method=="POST":
			try:
				user=User.objects.get(email=request.POST['email'])
				otp=random.randint(1000,9999)
				subject = 'OTP for forgot password'
				message = 'Hello '+user.fname+'your OTP for forgot password Is : '+str(otp)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user.email,]
				send_mail( subject, message, email_from, recipient_list )
				return render(request,'otp.html',{'email':user.email,'otp':otp})
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
		user=User.objects.get(email=email)
		user.password=np
		user.save()
		msg="update password sucessfully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="new password & confirm password not match"
		return render(request,'new-password.html',{'email':email,'msg':msg})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="updated profile sucessfully"
		return render(request,'profile.html',{'user':user,'msg':msg})
		
	else:
			return render(request,'profile.html',{'user':user})


def socity_member(request):
	if request.method=="POST":
		try:
			Member.objects.get(email=request.POST['email'])
			msg="email already registered"
			return render(request,'socity-member.html',{'msg':msg})
		except:
			Member.objects.create(
				fname=request.POST['fname'],
				lname=request.POST['lname'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				address=request.POST['address'],
				sname=request.POST['socity-name'],
				profile_pic=request.FILES['profile_pic'],
				)
			msg="sign up sucessfully"
			return render(request,'socity-member.html',{'msg':msg})
	else:
		return render(request,'socity-member.html')