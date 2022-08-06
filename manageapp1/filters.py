from django import forms

from manageapp1.models import Appointment, Complaints
import django_filters
from django_filters import CharFilter, filters


class PlaceFilter(django_filters.FilterSet):
    schedule__department__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search ', 'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = ('schedule__department__name',)


class ScheduleFilter(django_filters.FilterSet):
    department__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search department', 'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = ('department__name',)

class ComplaintsFilter(django_filters.FilterSet):
    department__name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search ', 'class': 'form-control'}))

    class Meta:
        model = Complaints
        fields = ('department__name',)

