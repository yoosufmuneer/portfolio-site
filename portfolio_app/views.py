from django.shortcuts import render
from portfolio_app.models import Projects
# Create your views here.
def project_index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def project_detail(request, pk):
    projects = Projects.objects.get(pk=pk)
    context = {
        'projects': projects
    }
    return render(request, 'project_detail.html', context)
