from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.utils import model_meta

from api.models import Cart, CartItem, ProductSku, User

from .product import ProductSkuDisplaySerializer
from .user import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    user = UserSerializer()
    total_quantity = serializers.IntegerField(required=False)
    total_amount = serializers.FloatField(required=False)

    class Meta:
        model = Cart
        fields = ["id", "user", "total_quantity", "total_amount"]

    def update(self, instance, validated_data):
        user = validated_data.pop("user")
        try:
            user = User.objects.get(pk=user["id"])
        except User.DoesNotExist:
            msg = _("User does not exist")
            raise serializers.ValidationError({"detail": msg})

        instance.user = user

        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if not (attr in info.relations and info.relations[attr].to_many):
                setattr(instance, attr, value)

        instance.save()
        return instance


class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    cart_id = serializers.CharField()
    product_sku = ProductSkuDisplaySerializer()
    quantity = serializers.IntegerField()
    subtotal = serializers.FloatField(required=False)

    class Meta:
        model = CartItem
        fields = ["id", "cart_id", "product_sku", "quantity", "subtotal"]

    def create(self, validated_data):
        cart_id = validated_data.pop("cart_id")
        product_sku = validated_data.pop("product_sku")

        cart = Cart.objects.get(id=cart_id)
        product_sku = ProductSku.objects.get(id=product_sku["id"])

        cart_item = CartItem.objects.filter(product_sku=product_sku).first()
        if cart_item:
            cart_item.quantity += validated_data["quantity"]
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(
                cart=cart, product_sku=product_sku, **validated_data
            )

        cart.total_quantity += cart_item.quantity
        cart.total_amount += cart_item.subtotal
        cart.save()

        return cart_item

    def update(self, instance, validated_data):
        cart_id = validated_data.pop("cart_id")
        product_sku = validated_data.pop("product_sku")

        cart = Cart.objects.get(pk=cart_id)
        product_sku = ProductSku.objects.get(pk=product_sku["id"])

        cart.total_quantity -= instance.quantity
        cart.total_amount -= instance.subtotal

        instance.product_sku = product_sku
        instance.cart = cart

        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if not (attr in info.relations and info.relations[attr].to_many):
                setattr(instance, attr, value)
        instance.save()

        cart.total_quantity += instance.quantity
        cart.total_amount += instance.subtotal
        cart.save()

        return instance
