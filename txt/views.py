from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.db.models import Q
from .models import TKjv
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'txt/index.html')

def about(request):
    return render(request, 'txt/about.html')

def SearchResultsView(request):
    query = request.POST['content']
    object_list = TKjv.objects.filter(Q(t__icontains=query))
    size_list = object_list.count()
    return render(request, 'txt/index.html', {'object_list':object_list, 'query':query, 'size_list':size_list})
