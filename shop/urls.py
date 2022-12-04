from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'api/categories', CategoryViewset, basename='category-viewset')
router.register(r'api/products', ProductViewset, basename='product-viewset')

urlpatterns = [
    path('', include(router.urls)),
    path("api/send-mail/", SendMailNow.as_view(), name="send-mail"),
    path("api/send-mail-later/", SendMailLater.as_view(), name="send-mail-later"),
]