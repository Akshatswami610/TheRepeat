from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def feedback(request):
    return render(request, 'feedback.html')