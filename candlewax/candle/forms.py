from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Reviews
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

        #     Валидатор на проверку длины поля title
        def clean_title(self):
            title = self.cleaned_data['title']
            print(len(title))
            if len(title) > 30:
                raise ValidationError('Длина превышает 200 символов')

            return title
