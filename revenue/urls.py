from django.urls import path

from revenue.views import RevenueStatisticViewSet

urlpatterns = [path("", RevenueStatisticViewSet.as_view(), name="revenue-list")]

app_name = "revenue"
