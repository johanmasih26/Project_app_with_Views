from django.shortcuts import render
from django.views import View
# Create your views here.
class test1View(View):

    def get(self, request, *args, **kwargs):
        # projects = Project.objects.all()
        # context = {'projects':projects}
        return render(request, 'test1.html')
