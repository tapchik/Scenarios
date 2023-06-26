from django.contrib import admin
from .models import AbstractTestSuite, TestPlan, TestPlanContent, TestSuite, TestCase, TestStep

# Register your models here.

admin.site.register(AbstractTestSuite)
admin.site.register(TestSuite)
admin.site.register(TestPlan)
admin.site.register(TestPlanContent)
admin.site.register(TestCase)
admin.site.register(TestStep)