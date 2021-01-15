from django import forms
from .models import Rooms

class IOForm(forms.Form):
    io = forms.BooleanField(required=False)

class IoDeviceForm(forms.Form):
    boardId = forms.CharField(max_length=50)
    pinAdress = forms.CharField(max_length=50)
    stateTc = forms.BooleanField(required=False)


class addRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ("__all__")
