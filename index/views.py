import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import ArtWork, ArtType
import operator

def home(request):
    tempList = ArtWork.objects.all().filter(art_type=1, column_number=1, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        paint_list1 = tempList
    else:
        paint_list1 = ArtWork.objects.all().filter(art_type=1, column_number=1).order_by('sort')[:5]
    tempList = ArtWork.objects.all().filter(art_type=1, column_number=2, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        paint_list2 = tempList
    else:
        paint_list2 = ArtWork.objects.all().filter(art_type=1, column_number=2).order_by('sort')[:5]
    tempList = ArtWork.objects.all().filter(art_type=1, column_number=3, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        paint_list3= tempList
    else:
        paint_list3 = ArtWork.objects.all().filter(art_type=1, column_number=3).order_by('sort')[:5]


    tempList = ArtWork.objects.all().filter(art_type=2, column_number=1, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        water_list1= tempList
    else:
        water_list1 = ArtWork.objects.all().filter(art_type=2, column_number=1).order_by('sort')[:5]
    tempList = ArtWork.objects.all().filter(art_type=2, column_number=2, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        water_list2= tempList
    else:
        water_list2 = ArtWork.objects.all().filter(art_type=2, column_number=2).order_by('sort')[:5]
    tempList = ArtWork.objects.all().filter(art_type=2, column_number=3, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        water_list3= tempList
    else:
        water_list3 = ArtWork.objects.all().filter(art_type=2, column_number=3).order_by('sort')[:5]


    
    tempList = ArtWork.objects.all().filter(art_type=3, column_number=1, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        graph_list1= tempList
    else:
        graph_list1 = ArtWork.objects.all().filter(art_type=3, column_number=1).order_by('sort')[:5]
    tempList = ArtWork.objects.all().filter(art_type=3, column_number=2, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        graph_list2= tempList
    else:
        graph_list2 = ArtWork.objects.all().filter(art_type=3, column_number=2).order_by('sort')[:5] 
    tempList = ArtWork.objects.all().filter(art_type=3, column_number=3, art_status=2).order_by('sort')
    if tempList.count() >= 3:
        graph_list3= tempList
    else:
        graph_list3 = ArtWork.objects.all().filter(art_type=3, column_number=3).order_by('sort')[:5] 

    des_list1 = ArtWork.objects.all().filter(art_type=4, column_number=1).order_by('sort')[:5]
    des_list2 = ArtWork.objects.all().filter(art_type=4, column_number=2).order_by('sort')[:5]
    des_list3 = ArtWork.objects.all().filter(art_type=4, column_number=3).order_by('sort')[:5]

    print_list1 = ArtWork.objects.all().filter(art_type=5, column_number=1).order_by('sort')[:5]
    print_list2 = ArtWork.objects.all().filter(art_type=5, column_number=2).order_by('sort')[:5]
    print_list3 = ArtWork.objects.all().filter(art_type=5, column_number=3).order_by('sort')[:5]


    return render(
        request,
        'index/index_home.html',
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


def more_images(request, art_type):
    list1 = ArtWork.objects.all().filter(art_type=art_type, column_number=1).order_by('sort') 
    list2 = ArtWork.objects.all().filter(art_type=art_type, column_number=2).order_by('sort')
    list3 = ArtWork.objects.all().filter(art_type=art_type, column_number=3).order_by('sort')
    
    artType = ArtType.objects.get(id=art_type)
    
    return render(
        request,
        'index/more_image.html',
        context = {
            'list1': list1,
            'list2': list2,
            'list3': list3,
            'artType': artType
        }
    )