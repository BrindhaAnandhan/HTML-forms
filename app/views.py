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

def emp(request):
    
    if request.method == 'POST':
        eno = request.POST['eno']
        ename = request.POST['ename']
        job = request.POST['job']
        mgr = request.POST['mgr']
        date = request.POST['date']
        comm = request.POST['comm']
        deptno = request.POST['deptno']
        dept_o = Dept.objects.get(Dno = deptno)
        eo = Emp.objects.get_or_create(Empno =eno, Ename = ename, Job = job, MGR = mgr, Hiredate = date, Comm = comm, Deptno = dept_o)[0]
        eo.save()
        Eo = Emp.objects.all()
        data = {'emp1': Eo}
        return render(request, 'display.html', data)
    else:
        Do = Dept.objects.all()
        data1 = {'emp': Do}
        return render(request, 'emp.html', data1)
