import django_filters
from .models import Post
from django.forms import DateInput


class PostFilter(django_filters.FilterSet):
    datetime = django_filters.DateFilter(field_name='date_add', widget=DateInput(attrs={'type': 'date'}),
                                         lookup_expr='gt', label='Позже даты')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок')
    author_name = django_filters.CharFilter(field_name='autor__user__username', lookup_expr='icontains', label='Автор')

