from django.db import models

# Create your models here.

class Dept(models.Model):
    Dno = models.IntegerField(primary_key = True)
    Dname = models.CharField(max_length = 100)
    Dloc = models.CharField(max_length = 100)

    def __str__(self):
        return self.Dname
    

class Emp(models.Model):
    Empno = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=100)
    Job = models.CharField(max_length=100)
    MGR = models.IntegerField()
    Hiredate = models.DateField(auto_now_add=True)
    Comm = models.IntegerField(default=0)
    Deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename 
