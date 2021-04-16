from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API VIew"""

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_api_view = [
            'Uses HTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]
        return Response({'message': 'Hello', 'an_api_view': an_api_view})

