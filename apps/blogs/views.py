from django.shortcuts import render, HttpResponse, redirect
def index( request ):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse( response )

def new( request ):
    response = "Placeholder to later display a NEW form to display a NEW blog"
    return HttpResponse( response )
    
def create( request ): 
    return redirect( index )

def show( request, number ):
    response = "Placeholder to later display blog " + number
    return HttpResponse( response )

def edit( request, number ):
    response = "Placeholder to edit blog " + number
    return HttpResponse( response )

def destroy( request, number ):
    return redirect( index )

# Create your views here.
