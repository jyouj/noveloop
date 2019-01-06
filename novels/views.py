from django.views import generic

from .models import Novel

class IndexListView(generic.ListView):
    template_name = "novels/index.html"
    model = Novel
    context_object_name = "novels"
