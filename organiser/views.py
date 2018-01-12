from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from django.shortcuts import redirect
from datetime import *
from .forms import EventForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import json
from rest_framework import generics
from .serializers import EventSerializer

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('auth_login')
    else:
        return redirect('month_view')

def auth_login(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home_view')
            loginform = AuthenticationForm(data=request.POST)
            if loginform.is_valid():
                username = loginform.cleaned_data.get('username')
                raw_password = loginform.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home_view')
        else:
            form = UserCreationForm()
            loginform = AuthenticationForm()
        return render(request, 'organiser/login.html', {'form': form, 'loginform': loginform})

def month_view(request):
    events = Event.objects.filter(creator=request.user)
    testevent = Event.objects.get(title='testevent')
    testtitle = 'test title'
    testeventjson = json.dumps('json test')
    return render(request, 'organiser/month_view.html', {'eventlist': events, 'testevent': testevent, 'testtitle': testtitle, 'testeventjson': testeventjson})

def week_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/week_view.html', {'events': events})

def day_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/day_view.html', {'events': events})

def createevent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('month_view')

    else:
        form = EventForm()
    return render(request, 'organiser/createevent.html', {'form': form})

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_event(self, serializer):
        serializer.save()
