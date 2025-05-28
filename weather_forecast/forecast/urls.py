from django.urls import path
from . import views


urlpatterns = [
    path('', views.addpage, name = 'home'),

    # path('new/', views.NewsListView.as_view(), name = 'new'),
]
