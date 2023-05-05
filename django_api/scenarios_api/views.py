from django.shortcuts import render
from .models import TestSuite

# Create your views here.

def getTestSuite(title: str) -> TestSuite:
    suite = TestSuite.objects.get(title=title)
    return suite