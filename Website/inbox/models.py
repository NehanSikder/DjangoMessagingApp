from django.db import models

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

	#Methods

	#def send_message()

	#def get_all_messages()
   def __str__(self):
    """
    String for representing the Model object
    """
    return '%s (%s)' % (self.sender,self.subject,self.content)

