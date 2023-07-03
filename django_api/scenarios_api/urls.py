from django.urls import path
from .views import ViewTestPlans, ViewTestPlan, ViewAllTestSuites, ViewTestSuite, ViewAllTestCases, ViewTestCase, ViewUpdateTestCase, ViewTestCaseStatus, ViewCreateTestCase

urlpatterns = [
    path('testplans', ViewTestPlans.as_view()), # no parameters
    path('testplan', ViewTestPlan.as_view()), # required parameter 'id'
    path('testsuite', ViewTestSuite.as_view()), # required parameters 'id', 'ver'
    path('testcase', ViewTestCase.as_view()), # required parameters 'suite_id', 'ver', 'step'
    path('change_testcase_status', ViewTestCaseStatus.as_view()), # required parameters 'suite_id', 'ver', 'step'
    path('testsuites', ViewAllTestSuites.as_view()), # to be deleted
    path('testcases', ViewAllTestCases.as_view()), # to be deleted
    path('update_testcase', ViewUpdateTestCase.as_view()), 
    path('create_testcase', ViewCreateTestCase.as_view()),
]