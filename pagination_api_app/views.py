from django.shortcuts import render
from pagination_api_app.models import Employee
from pagination_api_app.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from pagination_api_app.pagination import MyPagination
# Create your views here.
class EmployeePaginationCRUD(ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	pagination_class = MyPagination