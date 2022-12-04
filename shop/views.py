from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.utils import timezone
from .tasks import send_excel
from .serializers import *
import json

# Create your views here.

# Category Viewset
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return CreateCategorySerializer
        return CategorySerializer

    def get_queryset(self):
        if self.action in ("create", "update", "partial_update", "destroy", "detail", "retrieve"):
            return Category.objects.all()
        else:
            return Category.objects.filter(parent=None)



# Product Viewset
class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return CreateProductSerializer
        return ProductSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60))
    def dispatch(self, *args, **kwargs):
        return super(ProductViewset, self).dispatch(*args, **kwargs)


# APIView to send mail async
class SendMailNow(APIView):
    def post(self, request):
        if "email" not in request.data:
            return Response({"status":"Please pass email"})
        email = request.data["email"]
        send_excel.delay(email=email)
        return Response({"status":"email is sent"})


# APIView to send asyn mail after 2 mins
class SendMailLater(APIView):
    def post(self, request):
        if "email" not in request.data:
            return Response({"status":"Please pass email"})
        email = request.data["email"]
        schedule, _ = CrontabSchedule.objects.get_or_create(minute=timezone.now().minute + 2, 
                                                                hour=timezone.now().hour )

        PeriodicTask.objects.create(crontab=schedule, name='send-mail'+"-"+str(timezone.now()), task='shop.tasks.send_excel', kwargs=json.dumps({"email":email}))
        return Response({"status":"email is scheduled"})