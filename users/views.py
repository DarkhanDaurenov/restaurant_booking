from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from bookings.models import Booking


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=user_profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': user_profile,
        'bookings': bookings
    })


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=user_profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
