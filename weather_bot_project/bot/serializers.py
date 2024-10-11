from rest_framework import serializers

from bot.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'user_id', 'command', 'response', 'timestamp']