from django.shortcuts import render,redirect
from .models import User,product,Wishlist,Cart
import requests
import random
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://localhost:8000'

def validate_signup(request):
	email=request.GET.get('email')
	data={
	'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)


def validate_login(request):
	email=request.GET.get('email')
	data={
	'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)

def oldpass(request):
	oldpass=request.GET.get('oldpass')
	user=User.objects.get(email=request.session['email'])
	flag=False
	if user.password==oldpass:
		flag=True
	data={
	'is_taken':flag
	}
	return JsonResponse(data)

def validate_addpro(request):
	product_name=request.GET.get('addpro')
	seller=User.objects.get(email=request.session['email'])
	data={
	'is_taken':product.objects.filter(product_name__iexact=product_name,seller=seller).exists()
	}
	return JsonResponse(data)

@csrf_exempt
def create_checkout_session(request):
	amount = int(json.load(request)['post_data'])
	final_amount=amount*100
	
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'product_data': {
					'name': 'Checkout Session Data',
					},
				'unit_amount': final_amount,
				},
			'quantity': 1,
			}],
		mode='payment',
		success_url=YOUR_DOMAIN + '/success.html',
		cancel_url=YOUR_DOMAIN + '/cancel.html',)
	return JsonResponse({'id': session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts:
		i.payment_status=True
		i.save()
		
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html')

def cancel(request):
	return render(request,'cancel.html')


# Create your views here.
def index(request):
	products=product.objects.all()
	try:

		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			return render(request,'index.html',{'products':products})
		else:
			return render(request,'seller-index.html',{'products':products})
	except:
		return render(request,'index.html',{'products':products})

def seller_index(request):
	products=product.objects.all()
	seller=User.objects.get(email=request.session['email'])
	products=product.objects.filter(seller=seller)
	return render(request,'seller-index.html',{'products':products})

def checkout(request):
	return render(request,'checkout.html')



def signup (request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="email Alredy Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:	
				if request.POST['usertype']=="buyer":
					admin_access=True
				else:
					admin_access=False
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					usertype=request.POST['usertype']

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
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					wishlists=Wishlist.objects.filter(user=user)
					request.session['wishlist_count']=len(wishlists)
					carts=Cart.objects.filter(user=user,payment_status=False)
					request.session['cart_count']=len(carts)
					return redirect('index')
				else:
					if user.admin_access==True:

						request.session['email']=user.email
						request.session['fname']=user.fname
						request.session['profile_pic']=user.profile_pic.url
						return redirect('seller-index')
					else:
						msg="Your Admin Access is still not approved. please contact"
						return render(request,'login.html',{'msg':msg})
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
		return redirect('index')
	except:
		return render(request,'login.html')


def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password==request.POST['old-password']:
			if request.POST['new-password']==request.POST['cnew-password']:
				user.password=request.POST['new-password']
				user.save()
				return redirect('logout')
			else:
				msg="new password & confirm new password does not match"
				if user.usertype=="buyer":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'seller-change-password.html',{'msg':msg})
		else:
			msg="old password does not match"
			if user.usertype=="buyer":
				return render(request,'change-password.html',{'msg':msg})
			else:
				return render(request,'seller-change-password.html',{'msg':msg})
	else:
		if user.usertype=="buyer":
			return render(request,'change-password.html')
		else:
			return render(request,'seller-change-password.html')

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
		msg="update profile sucessfully"
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-profile.html',{'user':user,'msg':msg})
	else:
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user})
		else:
			return render(request,'seller-profile.html',{'user':user})

def forgot_password(request):
	if request.method=="POST":
		mobile=request.POST['mobile']
		try:
			user=User.objects.get(mobile=mobile)
			otp=random.randint(1000,9999)
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"mIk9Ya7tBzZTeAU5C3VGyLwJuRH8ogc2xrqnsKMdPSib6W0jNlQCyZJVL4px2luo8hKgraUk9b3GWejM","variables_values":str(otp),"route":"otp","numbers":str(mobile)}	
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			return render(request,'otp.html',{'otp':otp,'mobile':mobile})
		except:
			msg="mobile not registered"
			return render(request,'forgot-password.html',{'msg':msgs})

	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	mobile=request.POST['mobile']
	if otp==uotp:
		return render(request,'new-password.html',{'mobile':mobile})
	else:
		msg="invalid OTP"
		return render(request,'otp.html',{'otp':otp,'mobile':mobile,'msg':msg})

def new_password(request):
	mobile=request.POST['mobile']
	np=request.POST['new-password']
	cnp=request.POST['cnew-password']

	if np==cnp:
		user=User.objects.get(mobile=mobile)
		user.password=np
		user.save()
		msg="password update sucessfully"
		return render(request,'login.html',{'msg':msg})

	else:
		msg="new-password & confirm new-password does not match"
		return render(request,'new-password.html',{'mobile':mobile,'msg':msg})
		
def seller_add_product(request):
	seller=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		print(request.POST['product_category'])
		product.objects.create(
				seller=seller,
				product_category=request.POST['product_category'],
				product_name=request.POST['product-name'],
				product_price=request.POST['product-price'],
				product_desc=request.POST['product-desc'],
				product_image=request.FILES['product-image'],
			)
		msg="add product sucessfully"
		return render(request,'seller-add-product.html',{'msg':msg})
	else:
		return render(request,'seller-add-product.html')


def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=product.objects.filter(seller=seller)
	return render(request,'seller-view-product.html',{'products':products})


def seller_product_detail(request,pk):
	products=product.objects.get(pk=pk)
	return render(request,'seller-product-detail.html',{'products':products})


def seller_edit_product(request,pk):
	products=product.objects.get(pk=pk)
	if request.method=="POST":
		products.product_category=request.POST['product_category']
		products.product_name=request.POST['product-name']
		products.product_price=request.POST['product-price']
		products.product_desc=request.POST['product-desc']
		try:
			products.product_image=request.FILES['product-image']
		except:
			pass
		products.save()
		msg="product update sucessfully"
		return render(request,'seller-edit-product.html',{'products':products,'msg':msg})
	else:
		return render(request,'seller-edit-product.html',{'products':products})

def seller_delete_product(request,pk):
	products=product.objects.get(pk=pk)
	products.delete()
	return redirect('seller-view-product')


def seller_view_leptop(request):
	seller=User.objects.get(email=request.session['email'])
	products=product.objects.filter(seller=seller,product_category="laptop")
	return render(request,'seller-view-product.html',{'products':products})

def seller_view_accessories(request):
	seller=User.objects.get(email=request.session['email'])
	products=product.objects.filter(seller=seller,product_category="Accessories")
	return render(request,'seller-view-product.html',{'products':products})

def seller_view_camera(request):
	seller=User.objects.get(email=request.session['email'])
	products=product.objects.filter(seller=seller,product_category="Camara")
	return render(request,'seller-view-product.html',{'products':products})


def product_detail(request,pk):
	wishlist_flag=False
	cart_flag=False
	products=product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	try:
		Wishlist.objects.get(user=user,products=products)
		wishlist_flag=True
	except:
		pass
	try:
		Cart.objects.get(user=user,products=products,payment_status=False)
		cart_flag=True
	except:
		pass
	return render(request,'product-detail.html',{'products':products,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag})


def add_to_wishlist(request,pk):
	products=product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=user,products=products)
	return redirect('wishlist')

def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	request.session['wishlist_count']=len(wishlists)
	return render(request,'wishlist.html',{'wishlists':wishlists})


def remove_from_wishlist(request,pk):
	products=product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.get(user=user,products=products)
	wishlists.delete()
	return redirect('wishlist')

def add_to_cart(request,pk):
	products=product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(
		user=user,
		products=products,
		product_price=products.product_price,
		product_qty=1,
		total_price=products.product_price,
	)
	return redirect('cart')

def cart(request):
	net_price=0
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	for i in carts:
		net_price=net_price+i.total_price
	return render(request,'cart.html',{'carts':carts,'net_price':net_price})


def remove_from_cart(request,pk):
	products=product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.get(user=user,products=products,payment_status=False)
	carts.delete()
	return redirect('cart')

def change_qty(request):
	pk=int(request.POST['pk'])
	carts=Cart.objects.get(pk=pk,payment_status=False)
	product_qty=int(request.POST['product_qty'])
	carts.product_qty=product_qty
	carts.total_price=carts.product_price*product_qty
	carts.save()
	return redirect('cart')

def myorder(request):
		user=User.objects.get(email=request.session['email'])
		carts=Cart.objects.filter(user=user,payment_status=True)
		return render(request,'myorder.html',{'carts':carts})


def seller_view_order(request):
	myorder = []
	seller=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(payment_status=True)
	for i in carts:
		if i.products.seller == seller:
			myorder.append(i)
	return render(request,'seller-view-order.html',{'myorder':myorder})