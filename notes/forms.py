# forms.py
from django import forms
from .models import Note, Category
from django.db.models import UniqueConstraint

class NoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user) 
        self.fields['category'].empty_label = 'Choose category'

    class Meta:
        model = Note
        fields = ['title', 'content', 'category']   
        labels = {
            'title': 'Title',
            'content': 'Content',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your note here...'
            }),
            'category': forms.Select(attrs={        
                'class': 'form-select form-select-sm rounded-pill'
            }),
        }

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Category name'
            }
        )
    )
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Name'}


    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

    def clean_name(self):

        name = self.cleaned_data['name'].strip()
        if Category.objects.filter(user=self.user, name=name).exists():
            raise forms.ValidationError("You already have a category with this name.")
        return name

            


        