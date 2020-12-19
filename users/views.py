from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# Changing code to entertain user login request
def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


