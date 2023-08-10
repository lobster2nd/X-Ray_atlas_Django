from django import forms
from rest_framework.exceptions import ValidationError

from .models import *


class AddExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Не выбрана"

    class Meta:
        model = Examinations
        fields = ['cat', 'title', 'slug', 'content', 'image', 'video_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title