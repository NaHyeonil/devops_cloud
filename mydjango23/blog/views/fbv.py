from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from blog.forms import PostForm, SubscriberForm
from blog.models import Post, Subscriber


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()

    format = request.GET.get("format", "")

    if format == "xlsx":
        tabular_data = Post.get_tabular_data(post_qs, format="xlsx")
        return HttpResponse(tabular_data, content_type="application/vnd.ms-excel")
    elif format == "json":
        tabular_data = Post.get_tabular_data(post_qs, format="json")
        return HttpResponse(tabular_data, content_type="application/json")

    return render(
        request,
        "blog/post_list.html",
        {
            "post_list": post_qs,
        },
    )


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
        },
    )


def post_new(request: HttpRequest) -> HttpResponse:
    # request.method  # "GET", "POST"

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect("blog:post_detail", saved_post.pk)
    else:
        form = PostForm()

    return render(
        request,
        "blog/post_form.html",
        {
            "form": form,
        },
    )


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, f"#{pk} 포스팅을 저장했습니다.")
            return redirect(saved_post)
            # return redirect("blog:post_detail", saved_post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/post_form.html",
        {
            "form": form,
            "post": post,
        },
    )


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete() #실제로 db에 DELETE 쿼리를 실행
        messages.success(request, f"#{pk}포스팅을 삭제했습니다.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {
        "post": post,
    },)


subscriber_new = CreateView.as_view(
    model=Subscriber,
    form_class=SubscriberForm,
)