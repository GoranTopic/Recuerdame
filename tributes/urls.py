from django.urls import path, include
from .views import ( TributeDetailView, TributeListView, 
        TributeUpdateView, TributeDeleteView, TributeCreateView, create_view )



urlpatterns = [ 
        path('<int:memorial_pk>/list', TributeListView.as_view(), name='tribute_list'),
        path('<int:memorial_pk>/<int:pk>/detail', TributeDetailView.as_view(), name='tribute_detail'),
        path('<int:memorial_pk>/<int:pk>/update', TributeUpdateView.as_view(), name='tribute_update'),
        path('<int:memorial_pk>/<int:pk>/delete', TributeDeleteView.as_view(), name='tribute_delete'),
        path('<int:memorial_pk>/new', create_view, name='tribute_new'),
        ]

