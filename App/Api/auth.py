from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from App.Serelizer.accountserelizer import accountserelizers
from django.contrib.auth import authenticate
from App.utils.tokenjwt import create_access_token, create_refresh_token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny


class authis (APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')

        password = request.data.get('password')
        userauth = authenticate(username=username, password=password)

        if userauth:

            access = create_access_token(userauth.id)
            refresh = create_refresh_token(userauth.id)

            try:
                token = Token.objects.get(user=userauth)
                token.key = access
                token.save()
            except Token.DoesNotExist:
                Token.objects.create(user=userauth, key=access)

            return Response({'access': access, 'refresh': refresh, 'user_id': userauth.id, 'message': 'Success'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Invalid credentials', 'message': 'Failed'}, status=status.HTTP_406_NOT_ACCEPTABLE)
