from django.contrib.auth.models import User, Group
from rest_framework import serializers
from reservas.reservasapi.models import Merchant, MerchantItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchant
        fields = ('cnpj', 'name')


class MerchantItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchantItem
        fields = ('merchant', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'price', 'minimum_purchase', 'maximum_per_day')
