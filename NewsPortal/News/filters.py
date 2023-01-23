from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'header_post': ['icontains'],
            'post': ['exact'],
            'date_post': ['gt']
        }
