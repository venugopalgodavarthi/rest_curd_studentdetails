from rest_framework import serializers
from curd.models import student

        
class studentserializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields= '__all__' 
        
        