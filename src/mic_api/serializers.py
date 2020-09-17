from rest_framework import serializers

from . import models

class MessageSerializer(serializers.ModelSerializer):
    """A serializer for message object"""

    class Meta:
        model = models.Message
        # all model fields will be included
        fields = '__all__' 