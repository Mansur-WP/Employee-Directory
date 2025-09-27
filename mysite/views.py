from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee
# Create your views here.
def home(request):
    employess = Employee.objects.all()
    context = {
        'employees': employess,
    }
    
    return render(request, 'home.html', context)
    