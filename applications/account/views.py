from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializers, ChangePasswordSerializers
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self, request):
        serializers = RegisterSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('Вы успешно зарегестрировались вам отправленно письмо на почту', status=201)


class ActivateAPIView(APIView):
    def get(self, request,  activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Успешно')


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializers = ChangePasswordSerializers(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Вы успешно сменили пароль', status=200)
