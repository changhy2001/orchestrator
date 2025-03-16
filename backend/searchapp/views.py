from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # or allow any
from rest_framework import status
from .models import UserMeta
from .serializers import UserMetaSerializer

class SearchUserMetaAPIView(APIView):
    permission_classes = [IsAuthenticated]  # or use an alternative

    def get(self, request, *args, **kwargs):
        q = request.query_params.get("q", "")
        username_contains = request.query_params.get("username_contains", "")
        credentials_contains = request.query_params.get("credentials_contains", "")
        questions_contains = request.query_params.get("questions_contains", "")
        session_info_contains = request.query_params.get("session_info_contains", "")
        created_at_min = request.query_params.get("created_at_min", "")
        created_at_max = request.query_params.get("created_at_max", "")
        updated_at_min = request.query_params.get("updated_at_min", "")
        updated_at_max = request.query_params.get("updated_at_max", "")

        # Start with all UserMeta objects
        metadatas = UserMeta.objects.all()

        # Apply full-text search if query is provided
        if q:
            vector = SearchVector("user__username", "credentials", "questions", "session_info")
            query = SearchQuery(q)

            metadatas = (
                metadatas.annotate(rank=SearchRank(vector, query))
                .filter(rank__gte=0.001)
                .order_by("-rank")
            )

        # Additional filters
        if username_contains:
            metadatas = metadatas.filter(user__username__icontains=username_contains)
        if credentials_contains:
            metadatas = metadatas.filter(credentials__icontains=credentials_contains)
        if questions_contains:
            metadatas = metadatas.filter(questions__icontains=questions_contains)
        if session_info_contains:
            metadatas = metadatas.filter(session_info__icontains=session_info_contains)

        # Date range filters
        if created_at_min:
            metadatas = metadatas.filter(created_at__gte=parse_date(created_at_min))
        if created_at_max:
            metadatas = metadatas.filter(created_at__lte=parse_date(created_at_max))
        if updated_at_min:
            metadatas = metadatas.filter(updated_at__gte=parse_date(updated_at_min))
        if updated_at_max:
            metadatas = metadatas.filter(updated_at__lte=parse_date(updated_at_max))
        
        serializer = UserMetaSerializer(metadatas, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        # Option A: Let the client supply all fields.
        serializer = UserMetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SearchUserMetaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]  # or adjust as needed

    def get(self, request, pk, *args, **kwargs):
        meta = get_object_or_404(UserMeta, pk=pk)
        serializer = UserMetaSerializer(meta)
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        meta = get_object_or_404(UserMeta, pk=pk)
        meta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""
add more views here
class SearchUserMetaAPIView(APIView):"
"""