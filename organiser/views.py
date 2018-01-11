from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from django.shortcuts import redirect
from datetime import *
from .forms import EventForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    today = str(datetime.now())
    return render(request, 'organiser/month_view.html', {'events': events}, {'today': today})

def week_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/week_view.html', {'events': events})

def day_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/day_view.html', {'events': events})

def createevent(request):
    form = EventForm();
    return render(request, 'organiser/createevent.html', {'form': form})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.author = request.user
            activity.save()
            return redirect('homepage')

    else:
        form = EventForm()
    return render(request, 'calendar/event_edit.html', {'form': form})

def register(request):
    return render(request, 'calendar/register.html')
