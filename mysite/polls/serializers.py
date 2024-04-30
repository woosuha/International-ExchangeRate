from rest_framework import serializers
from .models import All_Data

class DataSerializers(serializers.ModelSerializer) :

    class Meta :
        model = All_Data
        fields = '__all__'