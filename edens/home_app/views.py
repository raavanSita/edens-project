from django.shortcuts import render
from .models import hotsale, slideHead , inner , catogeryTitle , arrivalsContent, MENS_catogery,WOMENS_catogery,KIDS_catogery,FOOTWEAR_catogery
# Create your views here.
def index(request):
    slideHead_object = slideHead.objects.all()
    inner_object = inner.objects.all()
    catogeryTitle_object = catogeryTitle.objects.all()
    arrivalsContent_object = arrivalsContent.objects.all()
    hotsale_object = hotsale.objects.all()

    context = {'slideHead':slideHead_object,
    'inner':inner_object,
    'catogery':catogeryTitle_object,
    'arrivalsContent':arrivalsContent_object,
    'hotsale':hotsale_object}
    return render(request,'base/index.html',context)

def mensWear(request):
    catogery_object= MENS_catogery.objects.all()
    context = {'mens':catogery_object}
    return render(request,'pages/mens.html',context)

def womensWear(request):
    catogery_object= WOMENS_catogery.objects.all()
    context = {'womens':catogery_object}
    return render(request,'pages/womens.html',context)
def kidsWear(request):
    catogery_object= KIDS_catogery.objects.all()
    context = {'kids':catogery_object}
    return render(request,'pages/kids.html',context)

def footWear(request):
    catogery_object= FOOTWEAR_catogery.objects.all()
    context = {'footwears':catogery_object}
    return render(request,'pages/footwears.html',context)