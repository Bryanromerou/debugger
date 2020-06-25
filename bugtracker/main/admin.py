from django.db import models
from django.contrib import admin
from .models import Bug
from tinymce.widgets import TinyMCE

class BugAdmin(admin.ModelAdmin):
    # fields = ["bug_title",               This way of doing it will not section off the models but the other way will.
    #           "bug_published",
    #           "bug_info"
    #           ]
    fieldsets = [
            ("Title/Date",{'fields':["bug_title","bug_published"]}),
            ("info",{'fields': ["bug_info"]})
            ]

    formfield_overrides = {
            models.TextField: {'widget':TinyMCE()} }
admin.site.register(Bug,BugAdmin)
