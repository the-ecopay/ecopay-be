from rest_framework import viewsets
from gemini_ai.models import ImageUploaded,RecognizedItem
from gemini_ai.serializers import RecognizedItemsSerializers
from rest_framework.permissions import AllowAny


class DetectImageView(viewsets.ModelViewSet):
    queryset=RecognizedItem.objects.all()
    serializer_class=RecognizedItemsSerializers
