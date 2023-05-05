from django.db import models

# Create your models here.

class TestSuite(models.Model):
    title = models.CharField(max_length=255)

class TestCase(models.Model):
    title = models.CharField(max_length=255)
    idea = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255)
    def __repr__(self) -> str:
        return f"TestCase(id={self.id}, title={self.title})"

class TestStep(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    step = models.IntegerField()
    action = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255, null=True)