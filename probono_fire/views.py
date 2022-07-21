

from django.shortcuts import render


def front_page(request):
    #return HttpResponse('히히')
    return render(request,'front_page.html')

