from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the exgame index.")

'''
class IndexView(generic.ListView):
    template_name = 'index.html'
'''