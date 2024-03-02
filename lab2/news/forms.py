from .models import art
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class artForm(ModelForm):
    class Meta:
        model = art
        fields = ['id', 'title', 'full_text', 'date']

        widgets = {
            "id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ответ'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите подробно Ваш запрос'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата отправления заявки'
            })
        }
