from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
def Fbv_string(request):
    return HttpResponse('<h1>This is Function Based-View</h1>')

def Fbv_html(request):
    return render(request,'Fbv_html.html')

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1> This is Class Basedview</h1>')
    
class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')
