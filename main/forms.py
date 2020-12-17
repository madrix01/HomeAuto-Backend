from django import forms
from .models import Rooms

class IOForm(forms.Form):
    io = forms.BooleanField(required=False)


class addRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ("__all__")
