from rest_framework import serializers 
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField(read_only=True, method_name="get_child_categories")

    class Meta:
        fields = ["id","name","description","subcategories"]
        model  = Category

    def get_child_categories(self, obj):
        serializer = CategorySerializer(instance=obj.children.all(), many=True)
        return serializer.data


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model  = Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model  = Product
        depth = 1
        



