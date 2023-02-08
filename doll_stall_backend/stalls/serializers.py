from rest_framework import serializers
from .models import Dolls

class DollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dolls.objects.all()
        fields = ['user_id','first_name','last_name','email','password','country','user_name','age']