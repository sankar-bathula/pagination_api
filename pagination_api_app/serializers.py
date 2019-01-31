from rest_framework.serializers import ModelSerializer
from pagination_api_app.models import Employee
class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		fields = "__all__"