from django.shortcuts import render

# Create your views here.
from .models import Inbox
from django.views import generic

class MessagesListView(generic.ListView):
    model = Inbox
    context_object_name = 'message_list' 
    def get_queryset(self):
        return Inbox.objects.filter(recepient="Receiver")

class MessageDetailView(generic.DetailView):
    model = Inbox