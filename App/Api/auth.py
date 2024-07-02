from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from App.Serelizer.accountserelizer import accountserelizers
from django.contrib.auth import authenticate
from App.utils.tokenjwt import create_access_token, create_refresh_token
from rest_framework import status


class authis (APIView):
    def post(self, request):
        username = request.data.get('usernames')
        password = request.data.get('passwords')
        user = authenticate(username=username, password=password)
        if user:
            acces = create_access_token(user.id)
            refresh = create_refresh_token(user.id)
            return Response({'acces': acces, 'refresh': refresh, 'user_id': user.id, 'message': 1}, status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid credentials', 'message': 0}, status.HTTP_406_NOT_ACCEPTABLE)
