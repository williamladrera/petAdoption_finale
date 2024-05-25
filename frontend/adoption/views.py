# adoption/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from .forms import BookingForm
import datetime  # Add this import statement

def home(request):
    return render(request, 'home/index.html')

def shop(request):
    return render(request, 'home/shop.html')

def pet(request):
    return render(request, 'home/pet.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Convert date and time fields to strings
            data['date'] = data['date'].isoformat() if isinstance(data['date'], (datetime.date, datetime.datetime)) else data['date']
            data['time'] = data['time'].isoformat() if isinstance(data['time'], (datetime.time, datetime.datetime)) else data['time']
            response = requests.post('http://localhost:4000/api/v1/book/create', json=data)
            if response.status_code == 201:
                messages.success(request, 'Your booking appointment is submitted successfully!')
            else:
                messages.error(request, 'There was an error submitting your booking. Please try again.')
            return redirect('book')
    return render(request, 'home/book.html', {'form': form})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Convert date and time fields to strings
            data['date'] = data['date'].isoformat() if isinstance(data['date'], (datetime.date, datetime.datetime)) else data['date']
            data['time'] = data['time'].isoformat() if isinstance(data['time'], (datetime.time, datetime.datetime)) else data['time']
            response = requests.post('http://localhost:4000/api/v1/book/create', json=data)
            if response.status_code == 201:
                messages.success(request, 'Your booking appointment is submitted successfully!')
            else:
                messages.error(request, 'There was an error submitting your booking. Please try again.')
        return redirect('book')
    return redirect('book')
