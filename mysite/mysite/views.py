from django.http import HttpResponse


def move_to_polls(request):
    return HttpResponse('If u want to see something you have to move to ".../polls/" or ".../admin/"')
