from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from spend.models import SpendStatistic
from revenue.models import RevenueStatistic


class SpendStatisticViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.spend1 = SpendStatistic.objects.create(
            name="Item1",
            date="2023-09-27",
            spend=10.0,
            impressions=100,
            clicks=10,
            conversion=2,
        )
        self.spend2 = SpendStatistic.objects.create(
            name="Item2",
            date="2023-09-27",
            spend=20.0,
            impressions=200,
            clicks=20,
            conversion=4,
        )
        self.spend3 = SpendStatistic.objects.create(
            name="Item3",
            date="2023-09-28",
            spend=5.0,
            impressions=50,
            clicks=5,
            conversion=1,
        )
        self.revenue1 = RevenueStatistic.objects.create(
            name="Item1", date="2023-09-27", revenue=25.0, spend=self.spend1
        )
        self.revenue2 = RevenueStatistic.objects.create(
            name="Item2", date="2023-09-27", revenue=50.0, spend=self.spend1
        )

    def test_get_spending_statistics(self):
        url = reverse("spend:spend-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Item1")
        self.assertEqual(response.data[0]["date"], "2023-09-27")
        self.assertEqual(response.data[0]["sum_spend"], "10.00")
        self.assertEqual(response.data[0]["sum_impressions"], 100)
        self.assertEqual(response.data[0]["sum_clicks"], 10)
        self.assertEqual(response.data[0]["sum_conversion"], 2)
        self.assertEqual(response.data[0]["sum_revenue"], "75.00")
