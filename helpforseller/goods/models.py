from django.db import models

# Create your models here.


class Seller(models.Model):
    """
    Модель продавца
    Основное применение — парсинг логов на отдельные элементы по указанному разделителю

    Attributes:
        name : str — имя продавца
        email : str — email продавца
        phone : str — телефон продавца
        address : str — адрес продавца
        description : str — описание продавца
        image : str — фото продавца
        rating : int — рейтинг продавца
    """

    rating = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    name = models.CharField(max_length=100, verbose_name="Имя")  # Имя
    email = models.EmailField(verbose_name="Email")  # Email
    phone = models.CharField(max_length=20, verbose_name="Телефон")  # Телефон
    address = models.CharField(max_length=200, verbose_name="Адрес")  # Адрес
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )  # Описание
    image = models.ImageField(
        blank=True, null=True, upload_to="images/"
    )  # Фото продавца
    rating = models.IntegerField(
        choices=rating, default=3, verbose_name="Рейтинг"
    )  # Рейтинг

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    """
    Модель категории

    Attributes:
        name : str — наименование
        description : str — описание
    """

    name = models.CharField(
        max_length=100, verbose_name="Наименование"
    )  # Наименование
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )  # Описание

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Good(models.Model):
    """
    Модель товара

    Attributes:
        name : str — наименование товара
        price : float — цена товара
        shipping_price : float — стоимость доставки
        description : str — описание товара
        image : object — фото товара
        seller : foreignKey Seller — продавец (каскадно удаление)
        category : foreignKey Category — категория (защита от удаления)
    """

    name = models.CharField(
        max_length=100, verbose_name="Наименование"
    )  # Наименование
    price = models.FloatField(verbose_name="Цена")  # Цена
    shipping_price = models.FloatField(
        verbose_name="Стоимость доставки"
    )  # Стоимость доставки
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание"
    )  # Описание
    image = models.ImageField(
        blank=True, null=True, upload_to="images/"
    )  # Фото товара
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, verbose_name="Продавец"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name
