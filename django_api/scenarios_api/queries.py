from .models import WorkItem, TestCase, TestStep

def RetrieveAllTestCases() -> dict:
    wis = WorkItem.objects.filter(type='TC')
    testcases = []
    for wi in wis:
        query = TestCase.objects.filter(workitem=wi).order_by('-version')
        if len(query) > 0:
            testcase = query[0]
            item = {}
            item['id'] = testcase.workitem.id
            item['version'] = testcase.version
            item['ident'] = testcase.ident
            item['title'] = testcase.title
            item['idea'] = testcase.idea
            item['expected_result'] = testcase.expected_result
            item['created'] = testcase.created
            testcases.append(item)
    return testcases

def RetrieveTestCase(id: str, ver: int = None) -> dict:
    wi = WorkItem.objects.get(id=id)
    match ver:
        case None:
            testcase = TestCase.objects.filter(workitem=wi).order_by('-version')[0]
        case _:
            testcase = TestCase.objects.get(workitem=wi, version=ver)
    steps = _GetTestSteps(testcase)

    testcase = {
        'id': id,
        'ident': testcase.ident,
        'version': testcase.version,
        'title': testcase.title,
        'idea': testcase.idea,
        'expected_result': testcase.expected_result,
        'steps': steps
    }
    return testcase

def CreateNewVersionOfTestCase(body: dict) -> TestCase:
    wi = WorkItem.objects.get(id=body['id'])
    # get 
    current_tcase = TestCase.objects.filter(workitem=wi).order_by('-version')[0]
    new_version = current_tcase.version + 1
    new_testcase = TestCase(workitem=wi, 
                 version = new_version,
                 title = body['title'],
                 idea = body['idea'],
                 expected_result = body['expected_result'])
    new_testcase.save()
    _SaveSteps(new_testcase, body['steps'])
    return new_testcase

def CreateNewTestCase(body: dict) -> TestCase:
    # creating new work item
    wi = WorkItem(type='TC')
    wi.save()
    # creating new test case
    new_testcase = TestCase(workitem=wi, 
                            version=1,
                            title=body['title'],
                            idea=body['idea'],
                            expected_result=body['expected_result'])
    new_testcase.save()
    # saving test steps
    _SaveSteps(new_testcase, body['steps'])
    return new_testcase

def _SaveSteps(test_case: TestCase, steps: dict) -> int:
    for item in steps:
        step = TestStep(test_case=test_case,
                        step=item['step'],
                        action=item['action'],
                        expected_result=item['expected_result'])
        step.save()
    return len(steps)

def NumberOfStepsInTestCase(test_case: TestCase) -> int: 
    number_of_steps = TestStep.objects.count(test_case)
    return number_of_steps

def _GetTestSteps(testcase: TestCase):
    steps_object = TestStep.objects.filter(test_case=testcase).order_by('step')
    steps = []
    for row in steps_object:
        step = dict()
        step['step'] = row.step
        step['action'] = row.action
        step['expected_result'] = row.expected_result
        steps.append(step)
    return steps

def TestCaseExists(id: str) -> bool:
    query_set = WorkItem.objects.filter(id=id)
    if len(query_set) <= 0:
        return False
    item = query_set[0]
    if item.type == 'TC':
        return True
    return False
        