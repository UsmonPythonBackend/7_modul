from rest_framework import serializers
from .models import Services, Business, Users, Clients, FAQs, Comments


class ServiceSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'title', 'description', 'image', 'status')


class BusinessSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'title', 'description','image','status')

class UserSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'image', 'level', 'status')


class ClientSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'first_name', 'last_name', 'image', 'comment', 'status')

class FaqSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = ('id', 'question', 'answer')

class CommentSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'service', 'client', 'comment', 'status')
