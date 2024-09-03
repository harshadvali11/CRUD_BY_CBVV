from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView
from app.models import *

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #ordering=['sname']
    #queryset=School.objects.filter(sname='Jspiders')
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'


'''
    def data(request):
        schools=School.objects.all()
        d={'schools':schools}
        return render(request,'htmlname.html',context=d)'''
