from django.urls import path
from . import views

#This App handles 4 URL's : for login, for signup, for logout, for password change

urlpatterns = [
    path('home/',views.submit_travel_info,name='home'),
    path('availability/',views.pool_availability,name='pool_availability'),
    path('success/',views.form_success,name='success'),
]