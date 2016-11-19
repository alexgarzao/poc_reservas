from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from reservas.reservasapi.serializers import UserSerializer, GroupSerializer, MerchantSerializer, MerchantItemSerializer
from reservas.reservasapi.models import Merchant, MerchantItem


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MerchantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows merchants to be viewed or edited.
    """
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = MerchantItem.objects.all()
    serializer_class = MerchantItemSerializer
