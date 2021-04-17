from rest_framework import generics, permissions

from .models import Enrollee
from .serializers import EnrolleeSerializer


class EnrolleeCreateView(generics.CreateAPIView):
    """Создает заявление о приеме абитуриента"""

    serializer_class = EnrolleeSerializer
    permission_classes = (permissions.IsAuthenticated,)
