from django.shortcuts import render

# Create your views here.

def index(request): 
    # the homepage for learning logs

    return render(request, 'learning_logs/index.html')

