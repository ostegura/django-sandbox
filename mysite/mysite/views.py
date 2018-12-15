from django.http import HttpResponse


def index(request):
    return HttpResponse('If u want to see something you have to move to ".../polls/" or ".../admin/"')
