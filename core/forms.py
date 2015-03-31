from django.contrib.auth.models import User
from core.models import PDPlan, ActionItem
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class PDPlanForm(ModelForm):

    class Meta:
        model = PDPlan
        exclude = ['parent']

ActionItemFormSet = inlineformset_factory(PDPlan, ActionItem)