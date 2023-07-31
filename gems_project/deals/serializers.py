from rest_framework import serializers

from deals.models import Customer, Gem


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')

    def get_gems(self, obj):
        gems = Gem.objects.filter(
            customers__in=Customer.objects.order_by(
                '-spent_money'
            ).exclude(pk=obj.pk)[:4]
        ).filter(pk__in=obj.gems.values('pk'))
        return list(map(str, gems))
