from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to= "profile_pic/",default="")
	usertype=models.CharField(max_length=100,default="buyer")
	admin_access=models.BooleanField(default=False)

	def __str__(self):
		return self.fname

class product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	choice1=(
		("laptop","laptop"),
		("Accessories","Accessories"),
		("Camara","Camara"),
	)
	product_category=models.CharField(max_length=100,choices=choice1)
	product_name=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/",default="")

	def __str__(self):
		return self.seller.fname+ "-"+self.product_name

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	products=models.ForeignKey(product,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.fname+" - "+self.products.product_name



class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	products=models.ForeignKey(product,on_delete=models.CASCADE)
	product_price=models.PositiveIntegerField()
	product_qty=models.PositiveIntegerField(default=1)
	total_price=models.PositiveIntegerField()
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+" - "+self.products.product_name
