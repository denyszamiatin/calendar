from django import forms


class DateForm(forms.Form):
    dt = forms.DateField(label='Date', input_formats=['%d.%m.%Y'])
    

class TaskForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)
