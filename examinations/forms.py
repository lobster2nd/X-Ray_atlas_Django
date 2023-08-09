from django import forms
from .models import *


class AddExamForm(forms.Form):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Область исследования', empty_label='Не выбрана')
    title = forms.CharField(max_length=255, label='Название исследования')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание исследования')
    is_published = forms.BooleanField(label='Опубликовать', required=False, initial=True)
