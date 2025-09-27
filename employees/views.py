from django.shortcuts import render
from .models import Employee
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    return render(request, 'employee_detail.html', {'employee': employee})