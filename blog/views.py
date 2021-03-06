from django.shortcuts import render
from django.http import HttpResponse
import os

from .models import Post

# Create your views here.

def post_list(request) :
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
    })

def download(request) :
    filepath = '/Users/shinjayne/Downloads/재경 연락처.xlsx'
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f :
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename = {}'.format(filename)
        return response
