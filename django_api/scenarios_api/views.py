import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import WorkItem, TestSuite, TestCase, TestStep
from . import queries #import RetrieveAllTestCases

# Create your views here.

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
        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=400)
        # extract parameters from request
        id = int(request.GET['id'])
        ver = int(request.GET['v']) if 'v' in request.GET else None
        # form and return testcase
        testcase = queries.RetrieveTestCase(id, ver)
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
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=400)
        # extract parameners from request
        id = int(request.GET['id'])
        
        wi = WorkItem.objects.get(id=id)
        suite = TestSuite.objects.get(workitem=wi)

        response = {
            'testsuite': {
                'id': suite.workitem.id,
                'ident': suite.workitem.ident,
                'title': suite.title,
                'description': suite.description,
            }
        }
        return JsonResponse(response, status=200)