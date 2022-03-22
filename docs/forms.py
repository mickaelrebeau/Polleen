from django import forms
from docs.models import Docs


class DocsModelForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = [
            'image',
            'title',
            'description',
            'author_1',
            'author_2',
        ]