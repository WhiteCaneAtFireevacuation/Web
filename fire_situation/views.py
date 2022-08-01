from django.shortcuts import render

# Create your views here.

def detail_main_page(request):
    return render(request,'detail_main_page.html')
