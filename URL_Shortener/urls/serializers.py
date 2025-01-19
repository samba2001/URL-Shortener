from rest_framework import serializers
from .models import AccessLog


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = ['id', 'url', 'timestamp', 'ip_address']  # List the fields you want to include
