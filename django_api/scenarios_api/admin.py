from django.contrib import admin
from .models import WorkItem, TestSuite, TestCase, TestStep

# Register your models here.

admin.site.register(WorkItem)
admin.site.register(TestSuite)
admin.site.register(TestCase)
admin.site.register(TestStep)