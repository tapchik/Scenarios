from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    can_edit = models.BooleanField(default=True)
    can_create = models.BooleanField(default=True)
    can_progress = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"User(login=\'{self.login}\')"

class AbstractTestSuite(models.Model):
    """
    Multiple versions of test suites with the same id can exist. 
    """
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return f"Abstract TS{str(self.id).zfill(6)}"

class TestSuite(models.Model):
    """
    Describes an unmodifiable version of a test suite. Can be mentioned across multiple test plans. 
    """
    abstract = models.ForeignKey(AbstractTestSuite, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    class Meta: 
        verbose_name_plural = "Test Suites"
        constraints = [
            models.UniqueConstraint(fields=['abstract', 'version'], name='unique_testsuite_version'),
        ]
    def __str__(self) -> str:
        return f"{self.ident}-v{self.version}: {self.title}"
    @property
    def ident(self) -> str:
        return f"TS{str(self.abstract.id).zfill(6)}"

class TestPlan(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name_plural = "Test Plans"
    def __str__(self) -> str:
        return f"TestPlan(id={self.id}, title=\'{self.title}\')"
    @property
    def ident(self):
        return f"TP{str(self.id).zfill(6)}"

class TestPlanContent(models.Model):
    plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    abstract_suite = models.ForeignKey(AbstractTestSuite, on_delete=models.CASCADE)
    version = models.PositiveIntegerField(null=True, blank=True)
    class Meta: 
        verbose_name_plural = "Test Plan Contents"
        constraints = [
            models.UniqueConstraint(fields=['plan', 'step'], name='unique_step_for_testplan'),
        ]
    def __str__(self) -> str:
        return f"TestPlan(id={self.id}) has step {self.step} with AbstractSuite(id={self.abstract_suite.id}) with version {self.version}"

class TestCase(models.Model):
    suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    idea = models.CharField(max_length=255, blank=True)
    expected_result = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name_plural = "Test Cases"
        constraints = [
            models.UniqueConstraint(fields=['suite', 'step'], name='unique_step_for_testsuite'),
        ]
    def __str__(self) -> str:
        return f"TestCase(suite={self.suite.ident}, step={self.step}, title=\'{self.title}\')"

class TestStep(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField()
    action = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255, blank=True)
    class Meta: 
        verbose_name_plural = "Test Steps"
        constraints = [
            models.UniqueConstraint(fields=['test_case', 'step'], name='unique_teststep_testcase_step'),
        ]
    def __str__(self) -> str:
        return f"{self.test_case.ident} has step {self.step}"