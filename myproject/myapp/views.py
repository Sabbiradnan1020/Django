
from django.http import HttpResponse



def courses(request):
    return HttpResponse("This is myapp courses page.")
def about(request):
    return HttpResponse("This is myapp about page.")
def home(request):
    return HttpResponse("This is page")

