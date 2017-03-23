from django.shortcuts import render, redirect, HttpResponse
from .models import Course
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    print context
    return render(request, 'classes/index.html', context)

def courseadd(request):
    Course.objects.create(name = request.POST['coursename'], info = request.POST['courseinfo'])
    print request.POST['coursename']
    print request.POST['courseinfo']
    return redirect('/')
