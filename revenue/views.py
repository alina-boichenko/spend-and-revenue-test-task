from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from revenue.models import RevenueStatistic
from revenue.serializers import RevenueStatisticSerializer


class RevenueStatisticViewSet(ListAPIView):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        queryset = (
            self.queryset.select_related("spend")
            .values("date", "name")
            .annotate(
                sum_revenue=Sum("revenue"),
                sum_spend=Sum("spend__spend"),
                sum_impressions=Sum("spend__impressions"),
                sum_clicks=Sum("spend__clicks"),
                sum_conversion=Sum("spend__conversion"),
            )
        )

        return queryset

    @extend_schema(
        description="Get a list of revenue statistics with aggregated sums of values."
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
