from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import HomePageContent
from .serializers import HomePageContentSerializer

class HomePageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        language = request.query_params.get('language', 'en')
        content = HomePageContent.objects.first()
        serializer = HomePageContentSerializer(content)
        data = serializer.data
        return Response({
            'title': data[f'title_{language}'],
            'description': data[f'description_{language}']
        })