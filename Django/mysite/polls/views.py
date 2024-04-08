from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow, world.")

def some_url(requeset):
    return HttpResponse("Some url을 구현.")