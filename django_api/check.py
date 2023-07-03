from django_api import asgi

from scenarios_api import  views
from scenarios_api.models import User, TestSuite, TestCase

#suite = views.getTestSuite("Авторизация")
#print(suite.id)

#tcase = TestCase(title="Авторизация под администратором")
#tcase.save()

#TestSuite.objects.all().delete()



for tcase in User.objects.all():
    print(tcase.id, tcase.title)
    
#tcase = TestCase.objects.get(id=1)