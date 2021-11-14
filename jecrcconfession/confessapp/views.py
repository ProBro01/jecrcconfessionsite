from django.shortcuts import redirect, render
from confessapp import models

# Create your views here.
def index(request):
    confessions = models.confession.objects.all().order_by("-timeofpublish", "-dateofpublish")
    context = {
        "allconfessions" : confessions,
    }
    return render(request, "showallconfessions.html", context)

def registerconfession(request):
    if request.method == 'POST':
        confessiondis = request.POST.get('confessiondiscription')
        confess = models.confession(discription=confessiondis)
        confess.save()
    return redirect("/")