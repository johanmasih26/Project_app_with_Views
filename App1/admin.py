from django.contrib import admin
from .models import Project, Review, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','description']

admin.site.register(Project, ProjectAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['project','body']

admin.site.register(Review, ReviewAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag, TagAdmin)





