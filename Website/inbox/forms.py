from django import forms
from .models import Inbox
    
class SendMessageForm(forms.ModelForm):
	class Meta:
		model = Inbox
		fields = ('recepient', 'subject', 'content',)