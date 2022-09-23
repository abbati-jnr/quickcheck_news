from news.models import NewsItem
from news.serializers import NewsItemSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class NewsItemList(ListCreateAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

    # filtering by type
    def get_queryset(self):
        queryset = NewsItem.objects.all()
        item_type = self.kwargs.get('type', None)
        if item_type:
            queryset = queryset.filter(type=item_type)
        return queryset

    # Nullifying hacker_news_id for API post because we check hacker_news_id to determine if news is from hackernews
    def perform_create(self, serializer):
        serializer.validated_data['hacker_news_id'] = None
        serializer.save()


class NewsItemEdit(RetrieveUpdateDestroyAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

    # update item that was created in API only
    def perform_update(self, serializer):
        if serializer.data['hacker_news_id'] is not None:
            raise ValidationError('You can\'t edit this item.')
        serializer.save()

    # delete item that was created in API only
    def perform_destroy(self, instance):
        if instance.hacker_news_id is not None:
            raise ValidationError('You can\'t delete this item.')
        instance.delete()
