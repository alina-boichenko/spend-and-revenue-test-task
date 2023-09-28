from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    sum_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)
    sum_spend = serializers.IntegerField()
    sum_impressions = serializers.IntegerField()
    sum_clicks = serializers.IntegerField()
    sum_conversion = serializers.IntegerField()

    class Meta:
        model = RevenueStatistic
        fields = [
            "id",
            "date",
            "name",
            "sum_revenue",
            "sum_spend",
            "sum_impressions",
            "sum_clicks",
            "sum_conversion",
        ]
