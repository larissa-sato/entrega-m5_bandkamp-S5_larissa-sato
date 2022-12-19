from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from .permissions import IsAccountOwner



class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()
