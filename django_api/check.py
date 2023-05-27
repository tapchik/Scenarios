from django_api import asgi

from scenarios_api import  views
from scenarios_api.models import WorkItem, TestSuite, TestCase

#suite = views.getTestSuite("Авторизация")
#print(suite.id)

#tcase = TestCase(title="Авторизация под администратором")
#tcase.save()

for tcase in TestCase.objects.all():
    print(tcase.id, tcase.title)
    
#tcase = TestCase.objects.get(id=1)

wi = WorkItem.objects.filter(id='000001')
print(wi)