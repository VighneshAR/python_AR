from django.http import HttpResponse

def home(request):
    return HttpResponse("My Django project is working 🚀")
