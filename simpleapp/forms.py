from django import forms
from .models import Post
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = [
            'name',
            'category',
            'content',
        ]
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        content = cleaned_data.get("content")
        
        if name == content:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data