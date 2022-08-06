from django.contrib import messages
from django.shortcuts import render, redirect

from .filters import ScheduleFilter
from .forms import *
from .models import Government, AppointmentSchedule


def gov_add(request):
    gov_form = GovernmentRegister()
    login_form = LoginRegister()
    if request.method == 'POST':
        gov_form = GovernmentRegister(request.POST)
        login_form = LoginRegister(request.POST)

        if gov_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_govt = True
            user.save()
            user1 = gov_form.save(commit=False)
            user1.user = user
            user1.save()

            return redirect('viewgov')

    return render(request, 'register.html', {'gov_form': gov_form, 'login_form': login_form})


def viewgov(request):
    data = Government.objects.all()

    return render(request, "table.html", {'data': data})


def dept_add(request):
    dept = DepartmentForm()
    if request.method == 'POST':
        dept = DepartmentForm(request.POST)
        if dept.is_valid():
            dept.save()
            return redirect('dept_view')

    return render(request, 'deptadd.html', {'dept': dept})


def dept_view(request):
    data = Department.objects.all()
    return render(request, 'depttable.html', {'data': data})


def complaints_view(request):
    data = Complaints.objects.all()
    return render(request, 'cmpview_table.html', {'data': data})


def schedule_add(request):
    form = ScheduleAdd()
    if request.method == 'POST':
        form = ScheduleAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' Schedule Added Successfully')
            return redirect('admin_schedule_view')
    else:
        form = ScheduleAdd()
    return render(request, 'admin_schedule_add.html', {'form': form})


def schedule(request):
    n = AppointmentSchedule.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=n)
    n = scheduleFilter.qs
    context = {
        'schedule': n,
        'scheduleFilter': scheduleFilter,
    }
    return render(request, 'admin_schedule_view.html', context)


def schedule_delete(request, id):
    n = AppointmentSchedule.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Schedule Deleted Successfully')
        return redirect('admin_schedule_view')
    # else:
    #     return redirect('admin_schedule_view')
