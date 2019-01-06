from django.urls import path

from novels import views

app_name = 'novels'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('new/', views.NovelCreateView.as_view(), name='new'),
]
