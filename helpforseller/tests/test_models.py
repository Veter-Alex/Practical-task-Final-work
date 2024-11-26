from django.test import TestCase
from goods.models import Category, Good, Seller

# Create your tests here.


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(
            name="столовые приборы",
            description="описание категории столовые приборы",
        )

    def test_name_value(self) -> None:
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, "столовые приборы")

    def test_name_label(self) -> None:
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Наименование")

    def test_description_value(self) -> None:
        category = Category.objects.get(id=1)
        self.assertEqual(
            category.description, "описание категории столовые приборы"
        )

    def test_description_label(self) -> None:
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "Описание")

    def test_max_length(self) -> None:
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)


class SellerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Seller.objects.create(
            name="Сунь Чи",
            email="sunchi@example.com",
            phone="89999999999",
            address="China, Beijing",
            description="Хороший продавец",
            rating=5,
        )

    def test_name_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.name, "Сунь Чи")

    def test_name_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Имя")

    def test_email_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.email, "sunchi@example.com")

    def test_email_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "Email")

    def test_phone_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.phone, "89999999999")

    def test_phone_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("phone").verbose_name
        self.assertEqual(field_label, "Телефон")

    def test_address_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.address, "China, Beijing")

    def test_address_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("address").verbose_name
        self.assertEqual(field_label, "Адрес")

    def test_description_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.description, "Хороший продавец")

    def test_description_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "Описание")

    def test_rating_value(self) -> None:
        seller = Seller.objects.get(id=1)
        self.assertEqual(seller.rating, 5)

    def test_rating_label(self) -> None:
        seller = Seller.objects.get(id=1)
        field_label = seller._meta.get_field("rating").verbose_name
        self.assertEqual(field_label, "Рейтинг")


class GoodModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
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

        Good.objects.create(
            name="Ложка столовая",
            price=100,
            shipping_price=50,
            description="описание товара",
            seller=Seller.objects.get(id=1),
            category=Category.objects.get(id=1),
        )

    def test_name_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.name, "Ложка столовая")

    def test_name_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Наименование")

    def test_price_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.price, 100)

    def test_price_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("price").verbose_name
        self.assertEqual(field_label, "Цена")

    def test_shipping_price_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.shipping_price, 50)

    def test_shipping_price_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("shipping_price").verbose_name
        self.assertEqual(field_label, "Стоимость доставки")

    def test_description_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.description, "описание товара")

    def test_description_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "Описание")

    def test_seller_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.seller, Seller.objects.get(id=1))

    def test_seller_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("seller").verbose_name
        self.assertEqual(field_label, "Продавец")

    def test_category_value(self) -> None:
        good = Good.objects.get(id=1)
        self.assertEqual(good.category, Category.objects.get(id=1))

    def test_category_label(self) -> None:
        good = Good.objects.get(id=1)
        field_label = good._meta.get_field("category").verbose_name
        self.assertEqual(field_label, "Категория")

    def test_max_length(self) -> None:
        good = Good.objects.get(id=1)
        max_length = good._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)
