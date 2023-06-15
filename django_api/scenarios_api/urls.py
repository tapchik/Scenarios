from django.urls import path
from .views import ViewTestPlans, ViewTestPlan, ViewAllTestSuites, ViewTestSuite, ViewAllTestCases, ViewTestCase, ViewUpdateTestCase, ViewCreateTestCase

urlpatterns = [
    path('testplans', ViewTestPlans.as_view()), # no parameters
    path('testplan', ViewTestPlan.as_view()), # required parameter 'id'
    path('testsuite', ViewTestSuite.as_view()), # required parameters 'id' and 'ver'
    path('run_testcase', ViewTestCase.as_view()), # required parameters 'suite_id' and 'step'
    path('testsuites', ViewAllTestSuites.as_view()), # to be deleted
    path('testcases', ViewAllTestCases.as_view()), # to be deleted
    path('update_testcase', ViewUpdateTestCase.as_view()), 
    path('create_testcase', ViewCreateTestCase.as_view()),
]