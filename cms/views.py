# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import HomePageContent
# from .serializers import HomePageContentSerializer

# class HomePageAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         language = request.query_params.get('language', 'en')
#         content = HomePageContent.objects.first()
#         serializer = HomePageContentSerializer(content)
#         data = serializer.data
#         return Response({
#             'title': data[f'title_{language}'],
#             'description': data[f'description_{language}']
#         })

from rest_framework import generics, permissions
from .models import HomePageContent
from .serializers import HomePageContentSerializer

class HomePageContentListCreateView(generics.ListCreateAPIView):
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = HomePageContent.objects.all()
        page_name = self.request.query_params.get('page_name', None)
        language = self.request.query_params.get('language', None)

        if page_name:
            queryset = queryset.filter(page_name=page_name)
        if language:
            queryset = queryset.filter(**{f'title_{language}__isnull': False})
        return queryset

class HomePageContentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer
    permission_classes = [permissions.IsAuthenticated]