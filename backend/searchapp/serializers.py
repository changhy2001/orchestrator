# data_views/serializers.py
from rest_framework import serializers
from .models import UserMeta

class UserMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMeta
        fields = [
            'id', 'username', 'questions', 'credentials', 'session_info', 
            'user_logs', 'created_at', 'updated_at'
        ]

"""
# add more class if needed
class Serializer2():

"""