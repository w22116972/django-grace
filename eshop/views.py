from django.shortcuts import render

from datetime import datetime
from django.shortcuts import render
#from eshop.views import hello_world, home


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def home(request):
    #post_list = Post.objects.all()
    return render(request, 'home.html', {
        #'post_list': post_list,
    })

