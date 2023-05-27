from django.urls import path
from .views import ViewAllTestSuites, ViewTestSuite, ViewAllTestCases, ViewTestCase

urlpatterns = [
    path('testsuites', ViewAllTestSuites.as_view()),
    path('testsuite', ViewTestSuite.as_view()), 
    path('testcases', ViewAllTestCases.as_view()),
    path('testcase', ViewTestCase.as_view()),
]