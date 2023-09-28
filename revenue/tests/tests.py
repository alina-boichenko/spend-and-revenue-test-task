from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from revenue.models import RevenueStatistic
from spend.models import SpendStatistic


class RevenueStatisticViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.spend1 = SpendStatistic.objects.create(
            name="Spending1",
            date="2023-09-27",
            spend=10.0,
            impressions=100,
            clicks=10,
            conversion=2,
        )
        self.revenue1 = RevenueStatistic.objects.create(
            name="Revenue1", date="2023-09-27", revenue=25.0, spend=self.spend1
        )
        self.revenue2 = RevenueStatistic.objects.create(
            name="Revenue1", date="2023-09-27", revenue=25.0, spend=self.spend1
        )

    def test_get_revenue_statistics(self):
        url = reverse("revenue:revenue-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Revenue1")
        self.assertEqual(response.data[0]["date"], "2023-09-27")
        self.assertEqual(response.data[0]["sum_revenue"], "50.00")
        self.assertEqual(response.data[0]["sum_spend"], 20)
        self.assertEqual(response.data[0]["sum_impressions"], 200)
        self.assertEqual(response.data[0]["sum_clicks"], 20)
        self.assertEqual(response.data[0]["sum_conversion"], 4)
