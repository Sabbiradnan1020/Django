from django.http import HttpResponse

def hompage(requst):
    return HttpResponse("This is homepage")


def contact(request):
    return HttpResponse("This is contact page")