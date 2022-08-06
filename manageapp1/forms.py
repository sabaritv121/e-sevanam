import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TimeInput

from manageapp1.models import Login, Government, Department, Complaints, User, AppointmentSchedule, Uploads


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)

# def phone_number_validator(value):
#     if not re.compile(r'^[7-9]\d{9}$').match(value):
#         raise ValidationError('This is Not a Valid Phone Number')
class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

class GovernmentRegister(forms.ModelForm):
    # contact_no = forms.CharField()
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Government
        fields = ('name', 'contact_number', 'email', 'address', 'department')


class DepartmentForm(forms.ModelForm):
    # contact_no = forms.CharField()

    class Meta:
        model = Department
        fields = ('name', 'place', 'contact_number', 'email')


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ('subject', 'department','complaint')

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Uploads
        fields = ('department','subject','document','email','contact_no')


# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Uploads
#         fields = ('subject','department','certificate')

class UserRegister(forms.ModelForm):

    # department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ('name', 'contact_no', 'email', 'address',)

class ScheduleAdd(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput,)
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = AppointmentSchedule
        fields = ('department', 'date', 'start_time', 'end_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")
        date = cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("End Time should be greater than start Time.")

        if date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past")
        return cleaned_data

class SubscribeForm(forms.Form):
    email = forms.EmailField()
