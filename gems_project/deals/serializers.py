from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')

    def get_gems(self, obj):
        gems = obj.gems.all()
        customers = Customer.objects.order_by(
            '-spent_money'
        ).exclude(pk=obj.pk).prefetch_related('gems')[:4]
        customer_gems = [
            {
                item['id'] for item in items
            } for items in [
                customer.gems.all().values() for customer in customers
            ]
        ]
        top_gems = set().union(*customer_gems)
        return [str(gem) for gem in gems if gem.pk in top_gems]
