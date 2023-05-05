from django_api import asgi

from scenarios_api import  views
from scenarios_api.models import TestSuite, TestCase

#suite = views.getTestSuite("Авторизация")
#print(suite.id)

#tcase = TestCase(title="Авторизация под администратором")
#tcase.save()

for tcase in TestCase.objects.all():
    print(tcase.id, tcase.title)
    
#tcase = TestCase.objects.get(id=1)