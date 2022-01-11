from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = movieticket
        fields = '__all__'