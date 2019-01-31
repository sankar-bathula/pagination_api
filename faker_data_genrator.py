import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pagination_api.settings')
import django
django.setup()
from pagination_api_app.models import *
from faker import Faker
from random import *
faker = Faker()
def populate(n):
	for i in range(n):
		fno = randint(1001, 9999)
		fname = faker.name()
		fesal = randint(10000, 35000)
		feaddr = faker.city()
		emp_record = Employee.objects.get_or_create(eno=fno, ename=fname, esal=fesal, eaddr=feaddr)
populate(120)