from .models import WorkItem, TestCase, TestStep

def GetAllTestCases() -> dict:
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

def GetTestCase(id: str, ver: int = None) -> dict:
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

def CreateNewVersionOfTestCase(id: str, body: dict):
    wi = WorkItem.objects.get(id=id)
    older_tcase = TestCase.objects.filter(workitem=wi).order_by('-version')[0]
    current_version = older_tcase.version
    new_testcase = TestCase(workitem=wi, 
                 version = current_version+1,
                 title = body['title'],
                 idea = body['idea'],
                 expected_result = body['expected_result'])
    new_testcase.save()

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
        