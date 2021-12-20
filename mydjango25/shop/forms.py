from django import forms
from django.views.generic import CreateView

from shop.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


review_new = CreateView.as_view(
    form_class=ReviewForm,
    success_url=revers_lazy("shop:shop_list"),
)
