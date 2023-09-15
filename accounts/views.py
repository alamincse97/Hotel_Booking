from django.shortcuts import render, redirect
from .forms import RegistrationForm
 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
 
def user_login(request):
    return render(request, 'accounts/signin.html')