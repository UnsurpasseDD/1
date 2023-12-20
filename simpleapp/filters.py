from django_filters import FilterSet
from .models import Post, Category


class PostFilter(FilterSet):
    class Meta:
        model = Post

        fields = {
            'name': ['icontains'],


        }