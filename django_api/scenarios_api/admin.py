from django.contrib import admin
from .models import User, AbstractTestSuite, TestPlan, TestPlanContent, TestSuite, TestCase, TestStep

# Register your models here.

admin.site.register(User)
admin.site.register(AbstractTestSuite)
admin.site.register(TestSuite)
admin.site.register(TestPlan)
admin.site.register(TestPlanContent)
admin.site.register(TestCase)
admin.site.register(TestStep)