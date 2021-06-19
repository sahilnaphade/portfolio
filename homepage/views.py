from django.shortcuts import render
from .models import experience, education, publication

# Create your views here.

def index(request):
    all_exp = experience.objects.all().order_by('-endDate')
    all_edu = education.objects.all().order_by('-passingYear')
    all_pubs = publication.objects.all()
    return render(request, 'index1.html', {'experience' : all_exp, 'education' : all_edu, 'publication' : all_pubs})