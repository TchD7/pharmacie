from .models import Pharms,Pharms_de_garde
from rest_framework import serializers
class PharmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharms
        fields = '__all__'
        depth = 2

class Pharms_de_gardeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharms_de_garde
        fields = ('pharm',)
        depth = 2