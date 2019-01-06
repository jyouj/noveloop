from django.urls import path

from novels import views

app_name = 'novels'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('new/', views.NovelCreateView.as_view(), name='new'),
    path('<int:novel_id>/', views.NovelDetailView.as_view(), name='novel_detail'),
]
