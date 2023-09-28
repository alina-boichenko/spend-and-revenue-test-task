from django.db.models import Sum, Subquery, OuterRef
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from spend.serializers import SpendStatisticSerializer


class SpendStatisticViewSet(ListAPIView):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        revenue_subquery = RevenueStatistic.objects.filter(spend=OuterRef("pk")).values(
            "revenue"
        )[:1]

        queryset = self.queryset.values("date", "name").annotate(
            sum_spend=Sum("spend"),
            sum_impressions=Sum("impressions"),
            sum_clicks=Sum("clicks"),
            sum_conversion=Sum("conversion"),
            sum_revenue=Subquery(revenue_subquery),
        )

        return queryset

    @extend_schema(
        description="Get a list of spending statistics with aggregated sums of values."
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
