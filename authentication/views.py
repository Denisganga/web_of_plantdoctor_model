# views.py
from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm  # Create a form for your registration fields

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('success_page')  # Change 'success_page' to the actual URL name or path
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
