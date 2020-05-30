from django.urls import path, include
from .views import ( TributeDetailView, TributeListView, 
        TributeUpdateView, TributeDeleteView, TributeCreateView )



urlpatterns = [ 
        path('list', TributeListView.as_view(), name='tribute_list'),
        path('<int:pk>/detail', TributeDetailView.as_view(), name='tribute_detail'),
        path('<int:pk>/update', TributeUpdateView.as_view(), name='tribute_update'),
        path('<int:pk>/delete', TributeDeleteView.as_view(), name='tribute_delete'),
        path('new', TributeCreateView.as_view(), name='tribute_new'),
        ]

