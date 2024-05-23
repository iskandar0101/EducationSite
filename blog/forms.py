from django import forms
from .models import ContactPage

class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "To'liq ismingiz "}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Sizning Email adresingiz'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fan nomi'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sizning Xabaringiz', 'rows': 4}),
        }
        labels = {
            'name': 'Ism va Familiya',
            'email': 'Email Address',
            'subject': 'Fan nomi',
            'message': 'Xabar',
        }
        error_messages = {
            'name': {
                'required': "Iltimos to'liq ismingizni kiriting",
            },
            'email': {
                'required': 'Iltimos emailingizni kiriting.',
                'invalid': 'Iltimos mavjud emailni kiriting',
            },
            'subject': {
                'required': 'Iltimos fan nomini kiriting.',
            },
            'message': {
                'required': 'Iltimos xabarni kiriting.',
            },
        }
