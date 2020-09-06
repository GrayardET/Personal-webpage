from django.shortcuts import render
from django.http import HttpResponse
from comments import models

# Create your views here.
def index(request):
    comments = models.Comments.objects.all()
    return render(request, "index.html", {'comments': comments})

