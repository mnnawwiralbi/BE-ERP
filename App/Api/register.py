from rest_framework import generics, status
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
from App.Serelizer.accountserelizer import accountserelizers
from rest_framework.permissions import AllowAny


class register (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = accountserelizers
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            query = self.get_queryset()
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data)
        except Exception as e:
            return JsonResponse({'message': 'Failed to fetch data', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'message': 'Success: Data created'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Failed to create data', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
