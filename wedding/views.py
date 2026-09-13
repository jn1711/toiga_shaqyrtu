from datetime import datetime

from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RSVPForm, WishForm
from .models import RSVPResponse


EVENT_DATE = datetime(2026, 10, 18, 18, 0, 0)


def home(request):
    form = RSVPForm()
    wish_form = WishForm()
    if request.method == 'POST':
        if request.POST.get('form_type') == 'wish':
            wish_form = WishForm(request.POST)
            if wish_form.is_valid():
                wish_form.save()
                return redirect(f"{reverse('home')}?sent=wish#wishes")
        else:
            form = RSVPForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(f"{reverse('home')}?sent=rsvp#rsvp")

    return render(request, 'wedding/home.html', {
        'form': form,
        'wish_form': wish_form,
        'event_date': EVENT_DATE,
        'couple_names': 'Нұрсұлтан және Айдана',
        'location': 'Алматы облысы Қаскелең қаласы Event Hall',
    })


def responses(request):
    responses_list = RSVPResponse.objects.all()
    return render(request, 'wedding/responses.html', {'responses': responses_list})
