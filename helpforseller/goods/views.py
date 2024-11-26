from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *


class GoodsView(APIView):
    def get(self, request: Request) -> Response:
        """
        Получить список товаров
        :param request: Объект запроса
        :return: Объект ответа со списком товаров
        """
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Создать новый товар
        :param request: Объект запроса
        :return: Объект ответа со списком товаров
        """
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GoodDetail(APIView):
    def get(self, request: Request, good_id: int) -> Response:
        """
        Получить товар по id
        :param request: Объект запроса
        :param good_id: Id товара
        :return: Объект ответа со списком товаров
        """
        good = Good.objects.get(id=good_id)
        serializer = GoodSerializer(good)
        return Response(serializer.data)

    def put(self, request: Request, good_id: int) -> Response:
        """
        Обновить данные товара по id
        :param request: Объект запроса
        :param good_id: Id товара
        :return: Объект ответа со списком товаров
        """
        good = Good.objects.get(id=good_id)
        serializer = GoodSerializer(good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request: Request, good_id: int) -> Response:
        """
        Удалить товар по id
        :param request: Объект запроса
        :param good_id: Id товара
        :return: Объект ответа со списком товаров
        """
        good = Good.objects.get(id=good_id)
        good.delete()
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)


class GoodsCategoryView(APIView):
    def get(self, request: Request, category_id: int) -> Response:
        """
        Получить список товаров для категории
        :param request: Объект запроса
        :param category_id: Id категории
        :return: Объект ответа со списком товаров
        """
        goods = Good.objects.filter(category_id=category_id)
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)


class GoodsSellerView(APIView):
    def get(self, request: Request, seller_id: int) -> Response:
        """
        Получить список товаров для продавца
        :param request: Объект запроса
        :param seller_id: Id продавца
        :return: Объект ответа со списком товаров
        """
        goods = Good.objects.filter(seller_id=seller_id)
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):
    def get(self, request: Request) -> Response:
        """
        Получить список категорий
        :param request: Объект запроса
        :return: Объект ответа со списком категорий
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Создать новую категорию
        :param request: Объект запроса
        :return: Объект ответа со списком категорий
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CategoryDetail(APIView):
    def get(self, request: Request, category_id: int) -> Response:
        """
        Получить категорию по id
        :param request: Объект запроса
        :param category_id: Id категории
        :return: Объект ответа с категорией
        """
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request: Request, category_id: int) -> Response:
        """
        Обновить категорию по id
        :param request: Объект запроса
        :param category_id: Id категории
        :return: Объект ответа с категорией
        """
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request: Request, category_id: int) -> Response:
        """
        Удалить категорию по id
        :param request: Объект запроса
        :param category_id: Id категории
        :return: Объект ответа со списком категорий
        """
        category = Category.objects.get(id=category_id)
        category.delete()
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SellersView(APIView):
    def get(self, request: Request) -> Response:
        """
        Получить список продавцов
        :param request: Объект запроса
        :return: Объект ответа со списком продавцов
        """
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Создать нового продавца
        :param request: Объект запроса
        :return: Объект ответа с данными нового продавца или ошибками валидации
        """
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SellerDetail(APIView):
    def get(self, request: Request, seller_id: int) -> Response:
        """
        Получить продавца по id
        :param request: Объект запроса
        :param seller_id: Id продавца
        :return: Объект ответа со списком продавцов
        """
        seller = Seller.objects.get(id=seller_id)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)

    def put(self, request: Request, seller_id: int) -> Response:
        """
        Обновить данные продавца по id
        :param request: Объект запроса
        :param seller_id: Id продавца
        :return: Объект ответа со списком продавцов
        """
        seller = Seller.objects.get(id=seller_id)
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
