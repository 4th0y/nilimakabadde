from django.contrib import messages as django_messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import MessageForm
from .models import Memory, Message, SiteConfig


def home(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            django_messages.success(request, "Your message was pinned to the wall!")
            return redirect(reverse("home") + "#wall")
    else:
        form = MessageForm()

    context = {
        "config": SiteConfig.load(),
        "memories": Memory.objects.all(),
        "wall_messages": Message.objects.filter(approved=True),
        "form": form,
    }
    return render(request, "party/home.html", context)
