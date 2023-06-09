from django.urls import path
from .views import ViewTestPlan, ViewAllTestSuites, ViewTestSuite, ViewAllTestCases, ViewTestCase, ViewUpdateTestCase, ViewCreateTestCase

urlpatterns = [
    path('testplan', ViewTestPlan.as_view()),
    path('testsuites', ViewAllTestSuites.as_view()),
    path('testsuite', ViewTestSuite.as_view()), 
    path('testcases', ViewAllTestCases.as_view()),
    path('testcase', ViewTestCase.as_view()),
    path('update_testcase', ViewUpdateTestCase.as_view()), 
    path('create_testcase', ViewCreateTestCase.as_view()),
]