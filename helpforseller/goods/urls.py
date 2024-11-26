from django.urls import path

from . import views

urlpatterns = [
    # все товары
    path("goods/", views.GoodsView.as_view(), name="goods"),
    # товары по категории
    path(
        "goods/categories/<int:category_id>/",
        views.GoodsCategoryView.as_view(),
        name="goods_category",
    ),
    # товары по продавцу
    path(
        "goods/sellers/<int:seller_id>/",
        views.GoodsSellerView.as_view(),
        name="goods_seller",
    ),
    # один товар по id
    path(
        "goods/<int:good_id>/",
        views.GoodDetail.as_view(),
        name="good_detail",
    ),
    # все категории
    path("categories/", views.CategoriesView.as_view(), name="categories"),
    # одна категория по id
    path(
        "categories/<int:category_id>/",
        views.CategoryDetail.as_view(),
        name="category_detail",
    ),
    # все продавцы
    path("sellers/", views.SellersView.as_view(), name="sellers"),
    # один продавец по id
    path(
        "sellers/<int:seller_id>/",
        views.SellerDetail.as_view(),
        name="seller_detail",
    ),
]
