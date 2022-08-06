from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from cmpmanagement1 import settings
from .filters import PlaceFilter, ComplaintsFilter
# from .forms import ReplyForm
from .forms import SubscribeForm
from .models import Complaints, Appointment, AppointmentSchedule, Uploads

@login_required(login_url='login_view')
def govt_home(request):
    return render(request, 'govbase.html')

@login_required(login_url='login_view')
def cmp_gov(request):
    n = Complaints.objects.all()
    complaintsFilter = ComplaintsFilter(request.GET, queryset=n)
    n=complaintsFilter.qs
    context = {
        'complaints': n,
        'complaintsFilter': complaintsFilter,
    }
    return render(request, 'govt_cmp_view1.html', context)

@login_required(login_url='login_view')
def reply_complaint(request, id):
    complaint = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('cmp_gov')
    return render(request, 'gov_cmp_reply.html', {'complaint': complaint})

@login_required(login_url='login_view')
def appointment_admin(request):
    p = Appointment.objects.all()
    placeFilter = PlaceFilter(request.GET, queryset=p)
    p = placeFilter.qs
    context = {
        'appointment': p,
        'placeFilter': placeFilter,
    }
    return render(request, 'govt_appointment.html', context)

@login_required(login_url='login_view')
def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')

@login_required(login_url='login_view')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')

@login_required(login_url='login_view')
def doc_view(request):
    uploads = Uploads.objects.all()
    return render(request,'gov_doc_view.html',{'uploads':uploads})


@login_required(login_url='login_view')
def certificate(request,id):
    uploads = Uploads.objects.get(id=id)
    # form = ReplyForm(instance=uploads or None)
    if request.method == 'POST':
        # form = ReplyForm(request.POST or None, request.FILES or None, instance=uploads or None)
        # c = request.POST.get("reply")
        p = request.POST.get("certificate")
        # uploads.reply = c
        uploads.certificate = p
        uploads.save()
        messages.info(request,'certificate/document is send to user')
        return redirect('cmp_gov')
    return render(request,'gov_certificate_issue.html', {'uploads':uploads})


@login_required(login_url='login_view')
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'sabaristv'
            message = 'Document verification compleated...Certificate will be send to registered email within 2 working days'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Email send succesfully!')
            return redirect('subscribe')
    return render(request, 'gmail.html', {'form': form})
#
# def entry(request,id):
#     uploads = Uploads.objects.get(id=id)
#     if request.method == 'POST':
#         form = ReplyForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('cmp_gov')
#     else:
#         form = ReplyForm()
#
#     return render(request, "entry.html", {
#         "form": form ,'uploads':uploads
#     })
# def single_page(request, id):
#     img = Uploads.objects.filter(id=id)
#     profile = Uploads.objects.filter(id = request.user.id)
#
#     context = { "img": img, "profile": profile}
#
#     return render(request, "main/single_page.html", context)
# def model_form_upload(request):
#     form = DocumentForm
#     u = request.user
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = u
#             obj.save()
#
#             return redirect('home')
#     else:
#              form = DocumentForm()
#     return render(request, 'user_uploadform.html', {'form': form})
