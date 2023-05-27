import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import WorkItem, TestSuite, TestCase, TestStep
from . import queries #import GetAllTestCases

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ViewAllTestCases(View): 
    def get(self, request):
        testcases = queries.GetAllTestCases()
        response = {}
        response['testcases'] = testcases
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
        testcase = queries.GetTestCase(id, ver)
        response = {}
        response['testcase'] = testcase
        return JsonResponse(response, status=200)
    
    def put(self, request):
        # check for request validity
        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=400)
        # extract parameters from request
        id = int(request.GET['id'])
        # validify body
        body = json.loads(request.body.decode('utf-8'))
        assert body['title']
        assert body['idea']
        # creating new version of test case
        exists = queries.TestCaseExists(id)
        if exists:
            queries.CreateNewVersionOfTestCase(id, body)
            message = "Ok, updated"
            status = 201
        else:
            message = "Something went wrong"
            status = 500
        # sending response
        response = {}
        response['message'] = message
        return JsonResponse(response, status=status)

class ViewAllTestSuites(View):
    def get(self, request):
        wis = WorkItem.objects.filter(type='TS')
        suites = []
        for wi in wis:
            query = TestSuite.objects.filter(workitem=wi).order_by('workitem')
            if len(query) > 0:
                suite = query[0]
                item = {}
                item['id'] = suite.workitem.id
                item['title'] = suite.title
                item['description'] = suite.description
                suites.append(item)
        
        response = {}
        response['testsuites'] = suites
        print(response)
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