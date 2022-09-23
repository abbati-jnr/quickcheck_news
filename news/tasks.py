from datetime import datetime
from news.models import NewsItem
from .api_utils import get_largest_item_id, get_item_by_id
from news.serializers import NewsItemSerializer
from celery import shared_task


@shared_task(name="sync_db")
def sync_db():
    news_ids = []
    largest_item_id = get_largest_item_id()

    for item in range((largest_item_id - 100), largest_item_id):
        news_ids.append(item)

    latest_ids = filter_ids(news_ids)  # removing ids already in db
    print(latest_ids)
    for item_id in latest_ids:
        item = get_item_by_id(item_id)
        item['time'] = datetime.utcfromtimestamp(item['time']).strftime('%Y-%m-%d %H:%M:%S')

        # replacing id from hackernews API with hacker_news_id to match the model field
        item['hacker_news_id'] = item['id']
        del item['id']
        serializer = NewsItemSerializer(data=item)
        if serializer.is_valid():
            serializer.save()


def filter_ids(news_ids):
    ids_to_remove = NewsItem.objects.filter(id__in=news_ids).values_list('id', flat=True)
    filtered_ids = [item_id for item_id in news_ids if item_id not in ids_to_remove]
    return filtered_ids
