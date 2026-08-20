from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "message", "color"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name", "maxlength": 80,
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Write something nice...", "rows": 3, "maxlength": 500,
            }),
        }
