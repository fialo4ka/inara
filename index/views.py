import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import ArtWork

def home(request):
    paint_list1 = ArtWork.objects.all().filter(art_type=1, column_number=1)
    paint_list2 = ArtWork.objects.all().filter(art_type=1, column_number=2)
    paint_list3 = ArtWork.objects.all().filter(art_type=1, column_number=3)
    
    water_list1 = ArtWork.objects.all().filter(art_type=2, column_number=1)
    water_list2 = ArtWork.objects.all().filter(art_type=2, column_number=2)
    water_list3 = ArtWork.objects.all().filter(art_type=2, column_number=3)
    
    graph_list1 = ArtWork.objects.all().filter(art_type=3, column_number=1)
    graph_list2 = ArtWork.objects.all().filter(art_type=3, column_number=2)
    graph_list3 = ArtWork.objects.all().filter(art_type=3, column_number=3)
    
    des_list1 = ArtWork.objects.all().filter(art_type=4, column_number=1)
    des_list2 = ArtWork.objects.all().filter(art_type=4, column_number=2)
    des_list3 = ArtWork.objects.all().filter(art_type=4, column_number=3)

    print_list1 = ArtWork.objects.all().filter(art_type=5, column_number=1)
    print_list2 = ArtWork.objects.all().filter(art_type=5, column_number=2)
    print_list3 = ArtWork.objects.all().filter(art_type=5, column_number=3)


    return render(
        request,
        'index/index_there.html',
        context = {
            'paint_list1': paint_list1,
            'paint_list2': paint_list2,
            'paint_list3': paint_list3,
            'water_list1': water_list1,
            'water_list2': water_list2,
            'water_list3': water_list3,
            'graph_list1': graph_list1,
            'graph_list2': graph_list2,
            'graph_list3': graph_list3,
            'des_list1': des_list1,
            'des_list1': des_list2,
            'des_list3': des_list3,
            'print_list1': print_list1,
            'print_list2': print_list2,
            'print_list3': print_list3
        }
    )