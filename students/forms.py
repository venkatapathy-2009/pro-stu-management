from django.forms import ModelForm
from .models import student
class stu_form(ModelForm):
    class Meta:
        model=student
        fields="__all__"