from django import forms
from .models import Message
class MsgForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = ['message']
        # fields = ['message', 'reciever']
