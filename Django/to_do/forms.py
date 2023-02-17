from django import forms


class NewTask(forms.Form):
    new_task = forms.CharField(label="Task", max_length=500, required=True)


class UpdateTask(forms.Form):
    updated_task = forms.CharField(
        label="Update", 
        max_length=500, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter New Task'})
    )
