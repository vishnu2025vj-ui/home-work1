from django.shortcuts import render
from .forms import RegistrationForm

def register_view(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            message = f"Thanks for registering, {full_name}!"
            form = RegistrationForm()  
    else:
        form = RegistrationForm()
    
    return render(request, 'register/register.html', {'form': form, 'message': message})
