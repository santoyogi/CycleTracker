from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.forms import UserCreationForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# Create your views here.
@login_required()
def input(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        notes = request.POST.get('notes', '')
        cycle = Cycle(start_date=start_date, end_date=end_date, notes=notes)
        cycle.save()
    return render(request, 'tracker/input.html')

@login_required()
def history(request):
    user_history = Cycle.objects.all()
    context = {
        'user_history': user_history,
    }

    return render(request, 'tracker/history.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account is created. You may now login.')
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


