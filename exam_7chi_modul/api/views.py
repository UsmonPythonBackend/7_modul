
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .serializer import ServiceSerializerWeb, BusinessSerializerWeb, UserSerializerWeb, FaqSerializerWeb, ClientSerializerWeb, CommentSerializerWeb
from .models import Services, Business, Users, FAQs, Clients, Comments



class ServiceViewsetWeb(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Services.objects.filter(status='pb')
#custom search
    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = self.get_queryset().filter(title__icontains=search_data)

        serializer = ServiceSerializerWeb(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET',])
    def buy(self, request, *args, **kwargs):
        service = self.get_object()
        service.buy += 1
        service.save()
        return Response(data={'purchased': service.buy})

    @action(detail=False, methods=['GET',])
    def null_buy(self, request, *args, **kwargs):
        services = self.get_queryset().filter(buy=0)
        serializer = ServiceSerializerWeb(services, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_buy(self, request, *args, **kwargs):
        services = self.get_queryset()
        for service in services:
            service.buy += 1
            service.save()
        return Response(data={"message": "all service purchased"})



class BusinessViewsetWeb(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Business.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = self.get_queryset().filter(title__icontains=search_data)

        serializer = BusinessSerializerWeb(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['GET',])
    def see(self, request, *args, **kwargs):
        business = self.get_object()
        business.see += 1
        business.save()
        return Response(data={'seen': business.see})

    @action(detail=False, methods=['GET',])
    def null_see(self, request, *args, **kwargs):
        businesses = self.get_queryset().filter(see=0)
        serializer = BusinessSerializerWeb(businesses, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_see(self, request, *args, **kwargs):
        businesses = self.get_queryset()
        for business in businesses:
            business.see += 1
            business.save()
        return Response(data={"message": "all business seen"})

class UserViewsetWeb(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Users.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = self.get_queryset().filter(title__icontains=search_data)

        serializer = UserSerializerWeb(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class ClientViewsetWeb(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Clients.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = self.get_queryset().filter(title__icontains=search_data)

        serializer = ClientSerializerWeb(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def buy(self, request, *args, **kwargs):
        client = self.get_object()
        client.buy += 1
        client.save()
        return Response(data={'purchased': client.buy})

    @action(detail=False, methods=['GET',])
    def null_buy(self, request, *args, **kwargs):
        clients = self.get_queryset().filter(buy=0)
        serializer = ServiceSerializerWeb(clients, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET',])
    def all_buy(self, request, *args, **kwargs):
        clients = self.get_queryset()
        for client in clients:
            client.buy += 1
            client.save()
        return Response(data={"message": "all service purchased"})

class FaqViewsetWeb(viewsets.ModelViewSet):
    queryset = FAQs.objects.all()
    serializer_class = FaqSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return FAQs.objects.filter(status='pb')

class CommentViewsetWeb(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Comments.objects.filter(status='pb')

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = self.get_queryset().filter(title__icontains=search_data)

        serializer = CommentSerializerWeb(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
