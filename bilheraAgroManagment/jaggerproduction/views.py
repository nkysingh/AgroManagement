from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Worker
from .forms import WorkerForm

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already taken')
        else:
            user = User.objects.create_user(
                username=email,  # Use email as the username
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            messages.success(request, 'Signup successful. Please log in.')
            return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('overview')
        else:
            messages.error(request, 'Invalid username or password')  # Error message for invalid login
    return render(request, 'login.html')

@login_required
def overview_view(request):
    return render(request, 'overview.html')  # Render the dashboard template

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def workers_list_view(request):
    workers = Worker.objects.all()
    return render(request, 'workers_list.html', {'workers': workers})

@login_required
def add_worker_view(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Worker added successfully.')
            return redirect('workers_list')
    else:
        form = WorkerForm()
    return render(request, 'add_worker.html', {'form': form})

@login_required
def edit_worker_view(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request, 'Worker updated successfully.')
            return redirect('workers_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'edit_worker.html', {'form': form})