from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

import logging

from .serializers import MessageSerializer
from .models import Message
from .utils import UserGroupPermission

logger = logging.getLogger(__name__)

# Create your views here.
class MessageViewSet(viewsets.ViewSet):
    """Get the messages in system"""

    def list(self, request):
        """Return the message of a client, site and product"""
        
        logger.info("message get")
        logger.info(request.user.id)
        if False == UserGroupPermission().hasPermissionForTheAction(request.user, 'getMessage'):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)