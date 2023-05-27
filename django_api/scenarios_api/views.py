from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import WorkItem, TestSuite, TestCase, TestStep

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ViewAllTestCases(View): 
    def get(self, request):

        wis = WorkItem.objects.filter(type='TC')

        testcases = []
        for wi in wis:
            query = TestCase.objects.filter(workitem=wi).order_by('-version')
            if len(query) > 0:
                testcase = query[0]
                item = {}
                item['id'] = testcase.workitem.id
                item['ident'] = testcase.ident
                item['title'] = testcase.title
                item['version'] = testcase.version
                testcases.append(item)
        
        response = {}
        response['testcases'] = testcases
        print(response)
        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestCase(View):

    def get(self, request):

        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=500)
        id = request.GET['id']
        id = int(id)
        
        wi = WorkItem.objects.get(id=id)
        testcase = TestCase.objects.filter(workitem=wi).order_by('-version')[0]
        steps_object = TestStep.objects.filter(test_case=testcase).order_by('step')

        steps = []
        for row in steps_object:
            step = dict()
            step['step'] = row.step
            step['action'] = row.action
            step['expected_result'] = row.expected_result
            steps.append(step)

        response = {
            'testcase': {
                'id': id,
                'ident': testcase.ident,
                'version': testcase.version,
                'title': testcase.title,
                'idea': testcase.idea,
                'expected_result': testcase.expected_result,
                'steps': steps
            },
        }
        return JsonResponse(response, status=201)

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
        return JsonResponse(response, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestSuite(View):

    def get(self, request):

        if 'id' not in request.GET:
            response = {"message": "Error, bring parameter 'id'"}
            return JsonResponse(response, status=500)
        id = request.GET['id']
        id = int(id)
        
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
        return JsonResponse(response, status=201)