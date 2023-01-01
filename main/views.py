from django.shortcuts import render, redirect
from .models import UserInfo
from .forms import TravelInfoForm
from django.contrib.auth.decorators import login_required
from .serializers import UserInfoSerializer
from rest_framework.response import Response
import datetime
# Create your views here.

def form_success(request):
    return render(request,'form_success.html')

@login_required
def submit_travel_info(request):
    user = request.user
    """try:
        user = UserInfo.objects.get(username=user.username)
        return redirect('../success/')
    except user.DoesNotExist:"""
    if request.method == "POST":
        form = TravelInfoForm(request.POST)
        if form.is_valid():
            data_dict = form.cleaned_data
            arrival = datetime.datetime.combine(data_dict['arrival_date'], data_dict['arrival_time'])
            new_data = {
                'username' : user.username,
                'email' : user.email,
                'arrival' : arrival,
                'phone_number' : data_dict['phone_number'],
                'preferred_transport' : data_dict['preferred_transport'],
                'destination' : data_dict['destination'],
            }
            serializer = UserInfoSerializer(data = new_data)
            if serializer.is_valid():
                new_data['submitted'] = True
                serializer = UserInfoSerializer(data = new_data)
                if serializer.is_valid():
                    serializer.save()
                    return redirect('../success/')
            else:
                return Response("Error")
    else:
        form = TravelInfoForm()
    return render(request,"travel_form.html",{'form':form})

@login_required
def pool_availability(request):
    user = request.user
    user_info = UserInfo.objects.get(username=user.username)
    user_destination = user_info.destination
    user_arrival = user_info.arrival
    potential_matches = UserInfo.objects.filter(destination=user_destination, arrival__lte = (user_arrival - datetime.timedelta(hours=1)))
    return render(request,"pool_availability.html",{'potential_matches':potential_matches})