from rest_framework import serializers
from .models import predictions

class predictionsSerializers(serializers.ModelSerializer):
    class meta:
        model=predictions
        fields='__all__'