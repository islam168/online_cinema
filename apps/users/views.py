from django.contrib.auth import authenticate
from rest_framework import response, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
)
from rest_framework.permissions import AllowAny
from core.permissions import IsOwner
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from apps.users.authentication import token_expire_handler, expires_in
from apps.users.models import User, Purchase, Subscription
from apps.users.serializers import (
    UserSerializer, UserAuthSerializer, UserCreateSerializer, PurchaseSerializer, SubscriptionSerializers,
    UserUpdateSerializer, UserChangePasswordSerializer
)


class UserAuthAPIVIew(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserAuthSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.data['email'],
            password=serializer.data['password'],
        )
        print(user)

        if not user:
            return Response(
                data={'detail': 'Invalid Credentials or activate account'},
                status=HTTP_404_NOT_FOUND,
            )

        token, _ = Token.objects.get_or_create(user=user)
        is_expired, token = token_expire_handler(token)
        user_serialized = UserSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=HTTP_200_OK)


class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get(self, request, *args, **kwargs):
        self.serializer_class = UserSerializer
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        self.serializer_class = UserUpdateSerializer
        return self.update(request, *args, **kwargs)


class UserChangePasswordAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    lookup_field = 'id'
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()

class PurchaseAPIView(CreateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


class SubscriptionAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
