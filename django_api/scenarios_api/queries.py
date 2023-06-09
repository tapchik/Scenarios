from .models import TestPlan, TestPlanContent, AbstractTestSuite, TestSuite, TestCase, TestStep

def RetrieveAllTestCases() -> dict:
    return None
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
    return None
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
    return None
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
    return None
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
    return None
    query_set = WorkItem.objects.filter(id=id)
    if len(query_set) <= 0:
        return False
    item = query_set[0]
    if item.type == 'TC':
        return True
    return False

def RetrieveTestPlan(plan_id: int) -> dict:
    """
    Returns information about a test plan with specified id in a form of dictionary. 
    """
    plan = TestPlan.objects.get(id=plan_id)
    item = {
        'plan_ident': plan.ident,
        'plan_id': plan.id,
        'title': plan.title,
        'date_created': plan.created,
    }
    return item

def GetTestSuitesInPlan(plan_id: int) -> list[TestSuite]:
    plan = TestPlan.objects.get(id=plan_id)
    contents = TestPlanContent.objects.filter(plan=plan).order_by('step')
    suites = []
    for content in contents:
        suite = _GetTestSuite(content.abstract_suite.id, content.version)
        suites.append(suite)
    return suites

def _GetTestSuite(suite_id: int, ver: int = None) -> TestSuite:
    """
    Returns specified Test Suite or the latest version if \'ver\' not provided. 
    """
    abstract_suite = AbstractTestSuite.objects.get(id=suite_id)
    match ver:
        case None:
            suite = TestSuite.objects.filter(abstract=abstract_suite).order_by('-version')[0]
        case _:
            suite = TestSuite.objects.get(abstract=abstract_suite, version=ver)
    return suite

def RetrieveTestSuite(step: int, suite_id: int, ver: int = None) -> dict:
    suite = _GetTestSuite(suite_id, ver)
    item = {
        'step': step, 
        'suite_ident': suite.ident if ver == None else suite.ident+f'_v{suite.version}',
        'suite_id': suite_id,
        'version': suite.version if ver != None else 'Fresh',
        'title': suite.title,
        'description': suite.description,
        'test_cases_finished': 44,
        'test_cases_total': 88,
    }
    return item