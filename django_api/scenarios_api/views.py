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
                item['code'] = testcase.workitem.code
                item['title'] = testcase.title
                item['version'] = testcase.version
                testcases.append(item)
        
        response = {}
        response['testcases'] = testcases
        print(response)
        return JsonResponse(response, status=201)

def NumberOfTestCases(item: str) -> int:
    test_cases = TestCase.objects.filter(item=item)
    number = len(test_cases)
    return number

@method_decorator(csrf_exempt, name='dispatch')
class ViewTestCase(View):

    def get(self, request):

        if 'code' not in request.GET:
            response = {"message": "Error, bring parameter 'code'"}
            return JsonResponse(response, status=500)
        code = request.GET['code']
        code = int(code)
        
        wi = WorkItem.objects.get(code=code)
        testcase = TestCase.objects.filter(workitem=wi).order_by('-version')[0]
        steps_object = TestStep.objects.filter(test_case=testcase).order_by('step')

        steps = []
        for row in steps_object:
            step = dict()
            step['step'] = row.step
            step['action'] = row.action
            step['expected_result'] = row.expected_result
            steps.append(step)
        
        f = [1, 2, 3]

        response = {
            'testcase': {
                'code': code,
                'version': testcase.version,
                'title': testcase.title,
                'idea': testcase.idea,
                'expected_result': testcase.expected_result
            },
            'steps': steps
        }
        return JsonResponse(response, status=201)
