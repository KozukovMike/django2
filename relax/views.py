from django.shortcuts import render
from .models import Slider, ContentHtml


# Create your views here.
def relax(request):
    slider_list = Slider.objects.all()
    text_list = ContentHtml.objects.all()
    objects = {
        'slider_list': slider_list,
        'text_list': text_list,
    }
    return render(request, './relax.html', objects)
