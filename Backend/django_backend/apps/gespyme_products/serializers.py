from rest_framework.serializers import ModelSerializer
from apps.gespyme_products.models import Product


class ProductSerializer(ModelSerializer):
    # Serializer Class for Product model
    class Meta:
        model = Product
        fields = '__all__'
        