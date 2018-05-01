from django.http import HttpResponse

def index(request):
    # place the breakpoint  on the next line and then step through to get the error
    body = request.body
    # if the breakpoint is placed on the line below, you shouldn't see any error
    return HttpResponse('')
