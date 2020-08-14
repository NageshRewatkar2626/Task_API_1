from rest_framework import serializers

from .models import EmployeeModel

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ('name','contact_no','email','password')