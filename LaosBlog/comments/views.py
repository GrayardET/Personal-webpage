from django.shortcuts import render, redirect
from . import models
import time


# Create your views here.
def post_comment(request):
    if not request.session.get('is_login'):
        return redirect('/User/login')
    if request.method == "POST":
        comment = models.Comments.objects.create()
        comment.content = request.POST.get('content')
        comment.user_id = request.session.get('user_id', 0)
        comment.save()
        return redirect('/')
