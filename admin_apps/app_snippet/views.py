from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import SnippetSerializer, TagSerializer

# Create your views here.
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [IsAuthenticated]


# class SnippetViewSet(viewsets.ModelViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         # Add user from the request
#         serializer.save(user=self.request.user)

class OverviewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_snippets = Snippet.objects.filter(created_by=request.user).count()
        snippets = Snippet.objects.filter(created_by=request.user)
        snippet_serializer = SnippetSerializer(snippets, many=True)
        
        data = {
            "total_count": total_snippets,
            "snippets": snippet_serializer.data
        }
        
        return Response(data)