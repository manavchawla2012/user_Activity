from rest_framework import authentication, exceptions
from rest_framework.permissions import IsAuthenticated, BasePermission
from user.models import CustomUser


class CustomAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.method == "GET":
            api_key = request.GET.get("api-key")
            if not api_key:
                raise exceptions.ParseError("api-key not Found")

            if len(api_key) != 64:
                raise exceptions.ParseError("Invalid API key")

            try:
                user = CustomUser.objects.get(api_key=api_key)
            except CustomUser.DoesNotExist:
                raise exceptions.NotFound("User Not found")
            return user, None
        else:
            raise exceptions.MethodNotAllowed("This Method Not Allowed")


class CustomPermission(IsAuthenticated):

    def has_permission(self, request, view):
        if request.user:
            return True
        else:
            return False