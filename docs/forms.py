from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class DocsModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'title',
            'description',
            'author name 1',
            'author name 2',
        ]