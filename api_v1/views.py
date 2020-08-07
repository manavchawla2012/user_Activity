from django.shortcuts import render
from rest_framework import mixins, generics
from django.http import JsonResponse
from user.models import CustomUser
from api_v1.serializers import *
from rest_framework.response import Response
# Create your views here.


class UserDetailsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserActivitySerializer

    def get(self, request, *args, **kwargs):
        data = self.list(request, *args, **kwargs).data
        if data:
            data = {
                "ok": True,
                "members": data
            }
        return Response(data)