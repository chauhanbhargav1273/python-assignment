from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('forgot-password',views.forgot_password,name='forgot-password'),
    path('verify-otp',views.verify_otp,name='verify-otp'),
    path('new-password',views.new_password,name='new-password'),
    path('profile',views.profile,name='profile'),
    path('socity-member',views.socity_member,name='socity-member'),
]
