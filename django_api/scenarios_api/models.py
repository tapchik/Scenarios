from django.db import models

# Create your models here.

class WorkItem(models.Model):

    TESTSUITE = "TS"
    TESTCASE = "TC"
    WORK_ITEMS_CHOICES = [(TESTSUITE, "TestSuite"), (TESTCASE, "TestCase")]

    code = models.AutoField(primary_key=True)
    type = models.CharField(max_length=2, choices=WORK_ITEMS_CHOICES)

    class Meta: 
        verbose_name_plural = "WorkItems"
    def __str__(self) -> str:
        return f"WorkItem(ident={self.ident})"
    @property
    def ident(self) -> str:
        return f"{self.type}{str(self.code).zfill(6)}"

class TestSuite(models.Model):
    workitem = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    class Meta: 
        verbose_name_plural = "TestSuites"
    def __str__(self) -> str:
        return f"{self.workitem.ident}: {self.title}"

class TestCase(models.Model):
    workitem = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    idea = models.CharField(max_length=255, blank=True)
    expected_result = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name_plural = "TestCases"
        constraints = [
            models.UniqueConstraint(fields=['workitem', 'version'], name='unique_testcase_workitem_version'),
        ]
    def __str__(self) -> str:
        return f"{self.ident}: {self.title}"
    @property
    def ident(self) -> str:
        return f"{self.workitem.ident}-v{self.version}"

class TestStep(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    action = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255, blank=True)
    class Meta: 
        verbose_name_plural = "TestSteps"
    def __str__(self) -> str:
        return f"{self.test_case.ident} has step {self.step}"