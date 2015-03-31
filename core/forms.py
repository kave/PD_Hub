from django.contrib.auth.models import User
from core.models import PDPlan, ActionItem
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms
from core.models import PDPlan



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class PDPlanForm(ModelForm):

    class Meta:
        model = PDPlan
        exclude = ['parent']

ActionItemFormSet = inlineformset_factory(PDPlan, ActionItem)

