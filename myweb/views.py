from django.http import HttpResponse
from django.shortcuts import render

def firstpage(request):
    #return HttpResponse('hello 51reboot!')
    return render(request, 'index.html')
