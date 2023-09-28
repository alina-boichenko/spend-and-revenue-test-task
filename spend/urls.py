from django.urls import path

from spend.views import SpendStatisticViewSet

urlpatterns = [path("", SpendStatisticViewSet.as_view(), name="spend-list")]

app_name = "spend"
