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

def RetrieveTestCase(suite_id: int, ver: int, step: int) -> dict:
    ver = 'Fresh' if ver == None else ver
    suite = _GetTestSuite(suite_id, ver)
    testcase = TestCase.objects.get(suite=suite, step=step)
    item = {
        'step': step,
        'title': testcase.title,
        'idea': testcase.idea,
        'finished': testcase.finished,
        'actionable_steps': testcase.actionable_steps,
        'expected_result': testcase.expected_result,
    }
    return item

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

def AbsentParams(given_params: list, expected_params: list) -> list:
    """
    ABANDONED. Returns a list of absent expected params among given params. 
    """
    absent = []
    for param in expected_params:
        if param not in given_params:
            pass

def RetrieveTestPlan(plan_id: int) -> dict:
    """
    Returns information about a test plan with specified id in a form of dictionary. 
    """
    plan = TestPlan.objects.get(id=plan_id)
    item = {
        'plan_ident': plan.ident,
        'plan_id': plan.id,
        'title': plan.title,
        'date_created': plan.created.strftime("%d %b %Y, %H:%M:%S"),
    }
    return item

def RetrieveTestSuitesInTestPlan(plan_id: int) -> dict:
    plan = TestPlan.objects.get(id=plan_id)
    contents = TestPlanContent.objects.filter(plan=plan).order_by('step')
    result = []
    for content in contents:
        suite = _GetTestSuite(content.abstract_suite.id, content.version)
        test_cases_finished = TestCase.objects.filter(suite=suite, finished=True).count()
        test_cases_total = TestCase.objects.filter(suite=suite).count()
        item = {
            'step': content.step,
            'suite_ident': suite.ident+' (Fresh)' if content.version == None else suite.ident+f' (ver {content.version})',
            'suite_id': suite.abstract.id,
            'version': content.version if content.version != None else 'Fresh',
            'title': suite.title,
            'description': suite.description,
            'test_cases_finished': test_cases_finished,
            'test_cases_total': test_cases_total,
        }
        result.append(item)
    return result

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

def RetrieveTestSuite(suite_id: int, ver: int = None) -> dict:
    """
    Returns information about specified version of a test_suite or the latest version. 
    """
    suite = _GetTestSuite(suite_id, ver)
    testcases = RetrieveTestCases(suite_id, ver)
    item = {
        'suite_ident': suite.ident+" (Fresh)" if ver == None else suite.ident+f'_v{suite.version}',
        'suite_id': suite_id,
        'version': suite.version if ver != None else 'Fresh',
        'title': suite.title,
        'description': suite.description,
        'test_cases_finished': len(list(filter(lambda x: x['finished'] == 'Finished', testcases))),
        'test_cases_total': len(testcases),
        'testcases': testcases,
    }
    return item

def RetrieveTestCases(suite_id: int, ver: int = None) -> dict:
    """
    Returns test cases withing specified suite. 
    """
    suite = _GetTestSuite(suite_id, ver)
    tcases = TestCase.objects.filter(suite=suite).order_by('step')
    result = []
    for tcase in tcases:
        item = {
            'step': tcase.step,
            'title': tcase.title,
            'idea': tcase.idea,
            'expected_result': tcase.expected_result,
            'n_actionable_steps': len(tcase.actionable_steps.splitlines()),
            'finished': 'Finished' if tcase.finished == True else 'Pending',
        }
        result.append(item)
    return result
