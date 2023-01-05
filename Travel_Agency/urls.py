from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name='home'),
    path("about/",views.about, name='about'),
    
    path("login/",views.login, name='login'),
    path("register/",views.register, name='register'),
    path("logout/",views.logout, name='logout'),
    path("user/profile",views.profile, name='profile'),
    
    path("destination/",views.destination, name='destination'),
    path("booking/history",views.booking_history, name='booking_history')
]
