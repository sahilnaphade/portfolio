from django.shortcuts import render
from .models import experience, education

# Create your views here.

def index(request):
    all_exp = experience.objects.all().order_by('-endDate')
    return render(request, 'index.html', {'experience' : all_exp})