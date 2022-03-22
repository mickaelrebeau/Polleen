from django import forms
from docs.models import Doc


class DocsModelForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = [
            'image',
            'title',
            'description',
            'author_1',
            'author_2',
        ]