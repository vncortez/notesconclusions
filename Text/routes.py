from rest_framework import routers

from Text.views import TextViewSet, TypesFoundViewSet



router = routers.DefaultRouter()
router.register(r'text', viewset=TextViewSet)
router.register(r'types', viewset=TypesFoundViewSet)