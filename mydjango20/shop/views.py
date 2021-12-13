from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ShopForm
from shop.models import Shop, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all() #.order_by("-id")

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__id=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html",{
        "category_list": category_qs,
        "shop_list":qs,
    })

# /shop/100/
def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })


# /shop/new/
def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError("곧 구현 예정")

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()

            tag_list = []
            tags = form.cleaned_data.get("tags", "")
            for word in tags.split(","):
                tag_name = word.strip()
                tag, __ = Tag.objects.get_or_create(name=tag_name)
                tag_list.append(tag)

            saved_post.tag_set.clear()  # 간단구현을 위해 clear 호출
            saved_post.tag_set.add(*tag_list)

            # shop_detail 뷰를 구현했다면 !!!
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })