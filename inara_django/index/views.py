import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
       return render(
        request,
        'index/index_there.html',
        {
            
        }
    )