from django.shortcuts import render
from .models import user
# Create your views here.
def index(request):
	if request.method=="POST":
		user.objects.create(
			pname=request.POST['pname'],
			)
		msg="product saved sucessfully"
		return render(request,'index.html',{'msg':msg})
	else:
		return render(request,'index.html')

