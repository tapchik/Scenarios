from django.urls import path
from .views import ViewAllTestCases, ViewTestCase

urlpatterns = [
    path('testcases', ViewAllTestCases.as_view()),
    path('workitem', ViewTestCase.as_view()),
]