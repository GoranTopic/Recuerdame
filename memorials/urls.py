from django.urls import path, include
from  .views import ( MemorialListView, MemorialDetailView,
                      MemorialCreateView, MemorialUpdateView,
                      MemorialDeleteView )

urlpatterns = [ 
        path('list', MemorialListView.as_view(), name='memorial_list'),
        path('<int:pk>/detail', MemorialDetailView.as_view(), name='memorial_detail'),
        path('<int:pk>/update', MemorialUpdateView.as_view(), name='memorial_update'),
        path('<int:pk>/delete', MemorialDeleteView.as_view(), name='memorial_delete'),
        path('new', MemorialCreateView.as_view(), name='memorial_new'),
        ]

