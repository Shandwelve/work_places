
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.request import Request

from job_offers.models import JobOffer
from .services import create


@api_view(['GET'])
def index(request: Request):
    return render(request, 'job_offers/list.html', {'offers': JobOffer.objects.all()})


@api_view(['POST'])
def store(request: Request):
    create(request.POST.get('position'), request.POST.get('company'))
    return redirect('job_offers.index')
