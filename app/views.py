from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.

def dept(request):
    
    if request.method == 'POST':
        dno = request.POST['dno']
        dn = request.POST['dn']
        dl = request.POST['dl']

        do = Dept.objects.get_or_create(Dno = dno, Dname = dn, Dloc = dl)[0]
        do.save()
        do1 = Dept.objects.all()
        data = {'do': do1}
        return render(request,'land.html', data)
    return render(request, 'dept.html')



