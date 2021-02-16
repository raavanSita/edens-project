from django.shortcuts import render
from .models import slideHead , inner , catogeryTitle , arrivalsContent
# Create your views here.
def index(request):
    slideHead_object = slideHead.objects.all()
    inner_object = inner.objects.all()
    catogeryTitle_object = catogeryTitle.objects.all()
    arrivalsContent_object = arrivalsContent.objects.all()
    context = {'slideHead':slideHead_object,
    'inner':inner_object,
    'catogery':catogeryTitle_object,
    'arrivalsContent':arrivalsContent_object}
    return render(request,'index.html',context)