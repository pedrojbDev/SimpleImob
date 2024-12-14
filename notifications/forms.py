# notifications/forms.py

from django import forms

class NotificationForm(forms.Form):
    notify = forms.BooleanField(required=False, label="Desejo receber uma notificação")
