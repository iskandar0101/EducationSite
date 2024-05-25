from django import forms
from .models import ContactPage , Comment , ReviewPost

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



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...', 'rows': 4}),
        }
        






class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['name', 'level', 'photo', 'about']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your level'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here...', 'rows': 4}),
        }
