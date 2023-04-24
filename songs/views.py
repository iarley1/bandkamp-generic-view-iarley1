from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 1


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer) -> None:
        pk = self.kwargs.get("pk")
        album = get_object_or_404(Album, pk=pk)

        serializer.save(album=album)
