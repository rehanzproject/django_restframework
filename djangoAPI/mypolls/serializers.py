from rest_framework import serializers
from .models import Matkul

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matkul
        fields = ['id','matkul', 'kodemk']