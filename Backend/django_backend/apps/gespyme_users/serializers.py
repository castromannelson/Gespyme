from rest_framework.serializers import ModelSerializer
from apps.gespyme_users.models import Gespyme_user

# User Serializer
class GespymeUserSerializerCretion(ModelSerializer):
    class Meta:
        model = Gespyme_user
        fields = '_all_'
    
    
