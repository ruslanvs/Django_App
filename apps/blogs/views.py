from django.shortcuts import render, HttpResponse, redirect
def index( request ):
    # response = "Placeholder to later display all the list of blogs"
    # return HttpResponse( response )
    return render( request, "blogs/index.html" )

def new( request ):
    response = "Placeholder to later display a NEW form to display a NEW blog"
    return HttpResponse( response )
    
def create( request ):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect( index )
    else:
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
