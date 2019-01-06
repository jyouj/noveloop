from django.shortcuts import redirect
from django.views import generic

from .models import Novel
from .forms import NewForm

# Chap.2-3
class IndexListView(generic.ListView):
    template_name = "novels/index.html"
    model = Novel
    context_object_name = "novels"

# Chap.2-4
class NovelCreateView(generic.CreateView):
    template_name = "novels/new.html"
    model = Novel
    form_class = NewForm

    def form_valid(self, form):
        novel = form.save(commit=False)
        novel.save()
        return redirect('novels:index')

# Chap.2-6
class NovelDetailView(generic.DetailView):
    template_name = "novels/novel_detail.html"
    model = Novel
    context_object_name = "novel"
    pk_url_kwarg = 'novel_id'
