from django.shortcuts import redirect
from django.views import generic

from .models import Novel

# Chap.2-3
class IndexListView(generic.ListView):
    template_name = "novels/index.html"
    model = Novel
    context_object_name = "novels"

# Chap.2-4
class NovelCreateView(generic.CreateView):
    template_name = "novels/new.html"
    model = Novel
    fields = ('title', 'text',)

    def form_valid(self, form):
        novel = form.save(commit=False)
        novel.save()
        return redirect('novels:index')
