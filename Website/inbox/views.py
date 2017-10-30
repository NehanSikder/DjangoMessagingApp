from django.shortcuts import render

# Create your views here.
from .models import Inbox
from django.views import generic

class MessagesListView(generic.ListView):
    model = Inbox
    context_object_name = 'message_list' 
    def get_queryset(self):
        return Inbox.objects.filter(recepient=self.request.user)

class MessageDetailView(generic.DetailView):
    model = Inbox

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.shortcuts import redirect


from .forms import SendMessageForm

# @permission_required('catalog.can_mark_returned')
def send_message(request):

    if request.method == "POST":
        print(request.user)
        form = SendMessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('send_message')
    else:
        form = SendMessageForm()
    return render(request, 'inbox/send_message.html', {'form': form})