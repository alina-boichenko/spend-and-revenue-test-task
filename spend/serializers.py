from rest_framework import serializers

from spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.ModelSerializer):
    sum_spend = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    sum_impressions = serializers.IntegerField()
    sum_clicks = serializers.IntegerField()
    sum_conversion = serializers.IntegerField()
    sum_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)

    class Meta:
        model = SpendStatistic
        fields = [
            "id",
            "date",
            "name",
            "sum_spend",
            "sum_impressions",
            "sum_clicks",
            "sum_conversion",
            "sum_revenue",
        ]
