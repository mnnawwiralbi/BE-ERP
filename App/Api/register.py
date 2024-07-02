from rest_framework import generics, status
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
# Pastikan ini sesuai dengan nama serializer Anda
from App.Serelizer.accountserelizer import accountserelizers


class register (generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = accountserelizers

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'message': 'Success: Data created'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Failed to create data', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework import status
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from django.contrib.auth.models import User
# from django.http.response import JsonResponse
# from App.Serelizer.accountserelizer import accountserelizers


# class register (generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = accountserelizers

#     def list(self, request, *args, **kwargs):
#         try:
#             query = self.get_queryset()
#             ser = self.get_serializer(data=query, many=True)
#             return Response(ser.data)
#         except:
#             return JsonResponse({'messsage': 'Failed Catch Data'})

#     def create(self, request, *args, **kwargs):
#         try:
#             account_serializer = self.get_serializer()
#             account_serializer(data=request.data)
#             if account_serializer.is_valid(raise_exception=True):
#                 self.perform_create(account_serializer)
#             return Response({'message': 'Succes Create Data'})
#         except:
#             return Response({'message': 'Failed Create Data'})
