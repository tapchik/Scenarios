import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import TestPlan, TestPlanContent, TestSuite, TestCase, TestStep
from . import queries #import RetrieveAllTestCases

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestPlans(View):
    def get(self, request):
        plans = TestPlan.objects.all().order_by('-created')
        response = {'testplans': []}
        for plan in plans:
            item = queries.RetrieveTestPlan(plan.id)
            suites = queries.RetrieveTestSuitesInTestPlan(plan.id)
            item['test_suites_finished'] = 0 # TODO
            item['test_suites_total'] = len(suites)
            response['testplans'] += [item]
        return JsonResponse(response, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestPlan(View):
    def get(self, request):
        # check for request validity
        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=400)
        # forming response
        plan_id = request.GET['id']
        plan = queries.RetrieveTestPlan(plan_id)
        response = { 'testplan': plan }
        testsuites = queries.RetrieveTestSuitesInTestPlan(plan_id)
        response['testplan']['testsuites'] = testsuites
        return JsonResponse(response, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class ViewAllTestCases(View): 
    def get(self, request):
        testcases = queries.RetrieveAllTestCases()
        response = {'testcases': testcases}
        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestCase(View):
    def get(self, request):
        # check for request validity
        if 'suite_id' not in request.GET:
            response = {"message": "Error, bring parameter 'suite_id'"}
            return JsonResponse(response, status=400)
        if 'ver' not in request.GET:
            response = {"message": "Error, bring parameter 'ver'"}
            return JsonResponse(response, status=400)
        if 'step' not in request.GET:
            response = {"message": "Error, bring parameter 'step'"}
            return JsonResponse(response, status=400)
        # extract parameters from request
        suite_id = int(request.GET['suite_id'])
        ver = int(request.GET['ver'])
        step = int(request.GET['step'])
        # form and return testcase
        testcase = queries.RetrieveTestCase(suite_id, ver, step)
        response = {'testcase': testcase}
        return JsonResponse(response, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class ViewUpdateTestCase(View):
    def put(self, request):
        # validate body
        body = json.loads(request.body.decode('utf-8'))
        # TODO validate body
        # refuse to update test case that doesn't exist
        exists = queries.TestCaseExists(body['id'])
        if exists != True:
            response = {'message': "Something went wrong"}
            return JsonResponse(response, status=500)
        # creating new version of test case
        new_testcase = queries.CreateNewVersionOfTestCase(body)
        number_of_steps = TestStep.objects.filter(test_case=new_testcase).count()
        response = {'message': f"Ok, new version of TestCase has been created: {new_testcase.ident} with {number_of_steps} steps"}
        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestCaseStatus(View):
    def put(self, request):
        # check for request validity
        if 'suite_id' not in request.GET:
            response = {"message": "Error, bring parameter 'suite_id'"}
            return JsonResponse(response, status=400)
        if 'ver' not in request.GET:
            response = {"message": "Error, bring parameter 'ver'"}
            return JsonResponse(response, status=400)
        if 'step' not in request.GET:
            response = {"message": "Error, bring parameter 'step'"}
            return JsonResponse(response, status=400)
        if 'finished' not in request.GET:
            response = {"message": "Error, bring parameter 'finished'"}
            return JsonResponse(response, status=400)
        # extract parameters from request
        suite_id = int(request.GET['suite_id'])
        ver = int(request.GET['ver']) if request.GET['ver'] != 'Fresh' else None
        step = int(request.GET['step'])
        # changing test case status
        suite = queries._GetTestSuite(suite_id, ver)
        tcase = TestCase.objects.get(suite=suite, step=step)
        tcase.finished = request.GET['finished']
        tcase.save()
        response = {'message': f"Ok, test case status has been changed. "}
        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ViewCreateTestCase(View):
    def post(self, request):
        # validate body
        body = json.loads(request.body.decode('utf-8'))
        # TODO validate body
        try: 
            new_testcase = queries.CreateNewTestCase(body)
            n_steps = queries.NumberOfStepsInTestCase(new_testcase)
            message = f"Ok, new TestCase {new_testcase.ident} with {n_steps} steps has been created"
            status = 201
        except:
            message = "There was an error creating new TestCase, we're so sorry"
            status = 500
        response = {'message': message}
        return JsonResponse(response, status=status)


class ViewAllTestSuites(View):
    def get(self, request):
        return None
        work_items = WorkItem.objects.filter(type='TS')
        suites = []
        for wi in work_items:
            query = TestSuite.objects.filter(workitem=wi).order_by('workitem')
            if len(query) > 0:
                suite = query[0]
                item = {}
                item['id'] = suite.workitem.id
                item['title'] = suite.title
                item['description'] = suite.description
                suites.append(item)
        response = {'testsuites': suites}
        return JsonResponse(response, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestSuite(View):
    def get(self, request):
        # check for request validity
        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'suite_id'"}
            return JsonResponse(response, status=400)
        if 'ver' not in request.GET:
            response = {"message": "Error, bring parameter 'ver'"}
            return JsonResponse(response, status=400)
        # extract parameners from request
        suite_id = int(request.GET['id'])
        ver = request.GET['ver'] if request.GET['ver'] != 'Fresh' else None
        suite = queries.RetrieveTestSuite(suite_id, ver)
        tcases = queries.RetrieveTestCases(suite_id, ver)
        response = {'testsuite': suite}
        return JsonResponse(response, status=200)