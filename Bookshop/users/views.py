from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from users.forms import ProfileAvatarForm, CustomUserCreationForm


@login_required
def profile_view(request):
    if request.method == 'GET':
        form = ProfileAvatarForm()
    else:
        form = ProfileAvatarForm(files=request.FILES, instance=request.user.profile)
        if form.is_valid:
            form.save()
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse(settings.LOGIN_REDIRECT_URL))

    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse(settings.LOGIN_REDIRECT_URL))

    return render(request, 'users/register.html', {
        'form': form
    })
