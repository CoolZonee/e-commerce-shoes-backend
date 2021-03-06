from django.db.models import fields
from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['upc', 'name', 'gender', 'color', 'price',
                  'cost', 'desc', 'brand', 'supplier', 'type', 'date', 'active', 'image_path']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailsRetrieveSerializer(serializers.ModelSerializer):
    product = ProductRetrieveSerializer(read_only=True)

    class Meta:
        model = ProductDetails
        fields = ['product', 'quantity', 'size']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
