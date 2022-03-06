from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from App1.forms import ProjectForm
from App1.models import Project, Tag


class projectsView(View):

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        context = {'projects':projects}
        return render(request, 'home.html', context)


class projectView(View):
    def get(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        # tags = project.tags.all()
        # reviews = project.reviews.all()
        context = {'project':project}
        return render(request, 'project_detail.html', context)

class projectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        context = {'form':form}
        return render(request, 'project_form.html', context)

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        return render(request, 'project_detail.html',{'form':form})



class projectUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        return render(request, 'project_form.html', {'form':form})

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        return render(request, 'project_form.html', {'form':form})


class projectDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        return render(request, 'project_delete.html', {'object':project})

    def post(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        project.delete()
        return redirect('projects')
        












