
from django.urls import path

from manageapp1 import views, admin_views, govt_views, user_views

urlpatterns = [
    path('', views.home,name='home'),
    path('login_view/', views.login_view, name='login_view'),
    # path('index', views.index, name="index"),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('gov', views.gov, name='gov'),
    path('admin_home', views.index, name='admin_home'),




    path('viewgov', admin_views.viewgov, name="viewgov"),
    path('govregister',admin_views.gov_add,name='govregister'),
    path('dept_add',admin_views.dept_add,name='dept_add'),
    path('dept_view',admin_views.dept_view,name='dept_view'),
    path('complaints',admin_views.complaints_view, name='complaints'),
    path('admin_schedule_add',admin_views.schedule_add, name='admin_schedule_add'),
    path('admin_schedule_view',admin_views.schedule, name='admin_schedule_view'),
    path('schedule_delete/<int:id>/', admin_views.schedule_delete, name='schedule_delete'),



    path('user_add',user_views.user_add, name='user_add'),
    path('user_cmpadd',user_views.user_cmpadd, name='user_cmpadd'),
    path('user_home',views.user, name = 'user_home'),

    path("upload",user_views.model_form_upload, name = 'upload'),

    path('cmp',user_views.complaint, name = 'cmp'),
    path('take_appointment/<int:id>/',user_views.take_appointment, name='take_appointment'),
    path('user_appointment',user_views.appointments,name='user_appointment'),
    path('schedule_user', user_views.schedule_user, name='schedule_user'),



    path('gov_home',govt_views.govt_home , name='gov_home'),
    path('cmp_gov', govt_views.cmp_gov, name = 'cmp_gov'),
    path('reply_complaint/<int:id>/', govt_views.reply_complaint, name='reply_complaint'),
    path('appointment_admin/', govt_views.appointment_admin, name='appointment_admin'),
    path('approve_appointment/<int:id>/', govt_views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', govt_views.reject_appointment, name='reject_appointment'),



    path('doc_view',govt_views.doc_view, name ='doc_view'),
    path('certificate/<int:id>/',govt_views.certificate,name='certificate'),
    # path('entry/<int:id>/', govt_views.entry, name='entry')
    path("mail", govt_views.subscribe, name='subscribe')

]
