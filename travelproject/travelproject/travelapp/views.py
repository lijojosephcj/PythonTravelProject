
from django.shortcuts import render
from .models import Place,Events
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Events.objects.all()
    return render(request, "index.html",{'result':obj,'res':obj1})


#def answer(request):
    #x = int(request.GET.get('num1'))
    #y = int(request.GET.get('num2'))
    #add = x + y
    #sub = x - y
    #mul = x * y
    #div = x / y
    #return render(request, "result.html", {'result1': add,'result2': sub,'result3': mul,'result4': div})
