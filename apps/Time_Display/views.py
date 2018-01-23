from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index ( request ):
    # response = "There we are"
    # return HttpResponse( response )
    context = {
        "time": strftime( "%Y - %m - %d %H:%M %p", gmtime() )
    }
    return render( request, "Time_Display/index.html", context )