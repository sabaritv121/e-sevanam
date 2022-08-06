from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .filters import ScheduleFilter
from .forms import LoginRegister, UserRegister, ComplaintForm, DocumentForm
from .models import Complaints, Appointment, AppointmentSchedule, User, Uploads


def user_add(request):
    form1=LoginRegister()
    form2=UserRegister()
    print(form2)
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
         form2 = UserRegister(request.POST)

         if form1.is_valid() and form2.is_valid():
                user = form1.save(commit=False)
                user.is_user = True
                user.save()
                user1 = form2.save(commit=False)
                user1.user = user
                user1.save()
                return redirect('home')

    return render(request, 'user_register.html', {'form1': form1, 'form2': form2})

@login_required(login_url='login_view')
def user_cmpadd(request):
    form=ComplaintForm
    u= request.user

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"complaint registered succesfully")
            return redirect('user_home')
    else:
        form = ComplaintForm()
    return render(request,'user_cmp_reg.html',{'form':form})


def complaint(request):
    n = Complaints.objects.filter(user=request.user)
    return render(request, 'user_cmp_view.html', {'complaint': n})

@login_required(login_url='login_view')
def schedule_user(request):
    s = AppointmentSchedule.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=s)
    s = scheduleFilter.qs
    context = {
        'schedule': s,
        'scheduleFilter': scheduleFilter,
    }
    return render(request, 'user_shedule.html', context)


@login_required(login_url='login_view')
def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('schedule_user')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('user_appointment')
    return render(request, 'take_appointment.html', {'schedule': schedule})


@login_required(login_url='login_view')
def appointments(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'user_appointment.html', {'appointment': a})


# def uploads(request):
#     form = Uploads()
#     if request.method == 'POST':
#         form = Uploads(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Documents Submitted Successfully')
#             return redirect('schedule_user')
#     return render(request, 'user_uploadform.html', {'form': form})



# def model_form_upload(request):
#
#
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#              form = DocumentForm()
#     return render(request, 'user_uploadform.html', {'form': form})


@login_required(login_url='login_view')
def model_form_upload(request):
    form = DocumentForm
    u = request.user
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()

            return redirect('user_home')
    else:
             form = DocumentForm()
    return render(request, 'user_uploadform.html', {'form': form})




