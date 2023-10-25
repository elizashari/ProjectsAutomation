from django import forms

from pr_auto.models import Student



class Project_Registration_Form(forms.ModelForm):
    # call_time = 
    class Meta:
        model = Student
        fields = ('email',)