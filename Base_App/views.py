from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import Item, ItemList, AboutUs, Feedback, BookTable
# Create your views here.

def HomeView(request):
    items = Item.objects.all()
    list = ItemList.objects.all()
    return render(request,'home.html', {'items':items, 'list':list})

def AboutView(request):
    return render(request,'about.html')

def MenuView(request):
    items = Item.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html', {'items':items, 'list':list})

def BookTableView(request):
    return render(request,'book_table.html')

def FeedbackView(request):
    return HttpResponse("Hi, this is my feedback page.")