from rest_framework import serializers
from django.contrib.auth import get_user_model
from hacker.models import NewsObject 

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields =['id','author','title','body','url','added', 'status', 'type']
        model =NewsObject
        
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','username',)