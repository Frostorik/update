from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'header_post',
            'type_post',
            'text_post',
        ]

    def clean(self):
        cleaned_data = super().clean()
        header_post = cleaned_data.get("header_post")
        if header_post is not None and len(header_post) < 3:
            raise ValidationError({
                "header_post": "Название записи не должно быть короче 3 символов."
            })

        return cleaned_data
