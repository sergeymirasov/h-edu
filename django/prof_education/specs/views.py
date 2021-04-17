from rest_framework import generics, permissions

from .models import Specialization
from .serializers import SpecializationSerializer


class SpecializationListView(generics.ListAPIView):
    """Получение списка специализаций с направлениями"""

    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
