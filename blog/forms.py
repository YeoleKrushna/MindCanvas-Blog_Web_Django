from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    """Form for Blog Post data"""
    class Meta:
        """Provide metadata about the form"""
        model = Post
        fields = ('title', 'body', 'image', 'categories')  # Add 'categories' here
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # Specifies the height
                'cols': 40,  # Specifies the width
                'placeholder': 'Enter your text here...'
            }),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),  # Multiple checkbox field for categories
        }

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),  # Get all categories from the database
        widget=forms.CheckboxSelectMultiple,  # Allows multiple checkboxes to be selected
        required=False  # Makes the category selection optional
    )
