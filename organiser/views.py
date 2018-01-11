from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event
from django.shortcuts import redirect

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('month_view')

def login(request):
    return render(request, 'organiser/login.html')

def month_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/month_view.html', {'events': events})

def week_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/week_view.html', {'events': events})

def day_view(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'organiser/day_view.html', {'events': events})

def createevent(request):
    return redirect('home_view')

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
