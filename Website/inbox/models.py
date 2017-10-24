from django.db import models
from django.urls import reverse
# Create your models here.
class Inbox(models.Model):
	"""
    Table that keeps track of all messages that have been sent between users
    """
    # Feilds
	recepient = models.CharField(max_length=20, help_text="receives message")
	sender = models.CharField(max_length=20, help_text="sent message")
	subject = models.CharField(max_length=78, help_text="summary of the message")
	content = models.TextField(help_text="content")

	def get_absolute_url(self):
		return reverse('message-detail', args=[str(self.id)])

	def __str__(self):
		return '%s - %s - %s ' % (self.sender,self.subject,self.content)

