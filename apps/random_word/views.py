from django.shortcuts import render, HttpResponse, redirect

def index ( request ):
    context = {
        "something": "we are here"
    }
    return render( request, "random_word/index.html", context )