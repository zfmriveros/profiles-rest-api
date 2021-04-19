from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API VIew"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_api_view = [
            'Uses HTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]
        return Response({'message': 'Hello', 'an_api_view': an_api_view})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """
    Test ApiViewSet
    """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        Return a hello message
        :param request:
        :return:
        """
        a_viewset = [
            'Users actions (list, create, retrieve, update, patial_update)',
            "Automatically maps URL using routers"
            'provide more functionality with list code'
        ]
        return Response({'message': 'Hello', 'view_set': a_viewset})

    def create(self, request):
        """
        Create a new hello message
        :param request:
        :return:
        """
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        :param request:
        :param ph:
        :return:
        """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """
        Updating object
        :param request:
        :param ph:
        :return:
        """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        Updating object partially
        :param request:
        :param ph:
        :return:
        """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        Remove object
        :param request:
        :param ph:
        :return:
        """
        return Response({'http_method': 'DELETE'})