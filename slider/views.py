from django.shortcuts import render
from .models import Slider

# Create your views here.


def home(request):
    slides = Slider.objects.filter(status=True, article__status=True)
    context = {
        'slides': slides
    }
    return render(request, 'slideShow.html', context)
