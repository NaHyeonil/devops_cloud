from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


def shop_list(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_list.html")


def shop_new(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_form.html")


def shop_detail(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_detail.html")


def shop_edit(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_detail.html")