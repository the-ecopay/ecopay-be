from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gemini_ai.views import *


router = DefaultRouter()
router.register(r'',DetectImageView)
urlpatterns = router.urls