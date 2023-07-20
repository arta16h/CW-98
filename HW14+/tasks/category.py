from django import forms
from .models import Category

class Create_Category(forms.ModelForm) :
    class Meta :
        model = Category
        fields = [
            "name"
        ]