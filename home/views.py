from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ads.models import Ads


def index(request):
    ads = Ads.objects.all()
    
    context = {
        'context_ads' : ads,
    }
    
    return render(request, 'index.html', context)


