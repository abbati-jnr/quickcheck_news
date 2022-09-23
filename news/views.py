from django.views.generic import ListView, DetailView
from .models import NewsItem
from django.db.models import Q


# Create your views here.


class NewsItemListView(ListView):
    model = NewsItem
    context_object_name = 'news_items'
    paginate_by = 30

    # filtering by type or text
    def get_queryset(self):
        queryset = NewsItem.objects.all()
        item_type = self.kwargs.get('type', None)
        item_text = self.request.GET.get('text', None)
        if item_type:
            queryset = queryset.filter(type=item_type)
        elif item_text:
            queryset = queryset.filter(Q(title__icontains=item_text) | Q(text__icontains=item_text))
        else:
            queryset = queryset.exclude(type='comment')

        return queryset


class NewsItemDetailView(DetailView):
    model = NewsItem
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = NewsItem.objects.filter(parent=self.object.id)
        return context
