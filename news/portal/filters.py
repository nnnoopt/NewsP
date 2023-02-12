from django_filters import FilterSet, CharFilter, DateFilter
from .models import *
import django.forms


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title', label='Заголовок', lookup_expr='icontains',
        widget=django.forms.TextInput(
            attrs={'typecategory_type': 'text', 'class': 'form-control', 'placeholder': "Веди текст..."}))

    date_time__gt = DateFilter(
        field_name="time", label="Дата", lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'category_type': 'date', 'class': "form-control"}))

class Meta:
    model = Post
    fields = ['title', 'author', 'date_time__gt']