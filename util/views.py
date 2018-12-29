from django.shortcuts import render


def homepage(request):
    print("entered homepage")
    return render(request, 'base.html')
