from django.contrib import admin
from .models import User,product,Wishlist,Cart

# Register your models here.
admin.site.register(User)
admin.site.register(product)
admin.site.register(Wishlist)
admin.site.register(Cart)

