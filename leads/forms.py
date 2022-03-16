from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Lead, Agent

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Lead


class LeadForm(forms.Form):
    profile_picture = forms.ImageField()
    logo = forms.ImageField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0, max_value=100)
    company = forms.CharField(max_length=100)
    post = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(min_length=0, max_length=10)
    communication_preference = forms.ChoiceField(
        choices=[(1, 'Email'), (2, 'SMS'), (3, 'Whatsapp'), (4, 'Polleen')])
    leisure = forms.CharField()
    linkedin = forms.URLField(max_length=100)
    facebook = forms.URLField(max_length=100)
    twitter = forms.URLField(max_length=100)
    instagram = forms.URLField(max_length=100)
    website = forms.URLField(max_length=100)
    other_social_media = forms.URLField(max_length=100)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['category']