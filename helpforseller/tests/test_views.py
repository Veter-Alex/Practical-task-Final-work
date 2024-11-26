from django.test import TestCase
from django.urls import reverse
from goods.models import Category, Good, Seller

# Create your tests here.


class GoodsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name="столовые приборы",
            description="описание категории столовые приборы",
        )

        Seller.objects.create(
            name="Сунь Чи",
            email="sunchi@example.com",
            phone="89999999999",
            address="China, Beijing",
            description="Хороший продавец",
            rating=5,
        )

        # Create 13 authors for pagination tests
        number_of_goods = 13
        for good_num in range(number_of_goods):
            Good.objects.create(
                name=f"Ложка столовая {good_num}",
                price=10,
                shipping_price=100,
                description=f"описание товара {good_num}",
                seller=Seller.objects.get(id=1),
                category=Category.objects.get(id=1),
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/goods/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("goods"))
        self.assertEqual(resp.status_code, 200)
