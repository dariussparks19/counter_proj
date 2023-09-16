from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    request.session['counter'] = 1 + request.session['counter']
    return render(request, 'index.html')

def destroy_session(request):
    del request.session['counter']
    return redirect('/')