from django.contrib import admin
from .models import TestSuite, TestCase, TestStep

# Register your models here.

admin.site.register(TestSuite)
admin.site.register(TestCase)
admin.site.register(TestStep)