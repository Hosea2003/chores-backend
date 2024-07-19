from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from identity.models import AppUser
from identity.serializers import AppUserDetailSerializer
from rest_framework.response import Response


# Create your views here.
class UserDetailsView(generics.GenericAPIView):
    """
    get authenticated user details
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AppUserDetailSerializer

    def get(self, request: Request, *args, **kwargs):
        user = request.user
        serializer = AppUserDetailSerializer(user)

        return Response(serializer.data)
