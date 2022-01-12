from django.shortcuts import render

from user.forms import UserSignupForm


def homepage(request):
    form = UserSignupForm()
    context = {
        'form': form
    }
    return render(request, 'base.html', context)
