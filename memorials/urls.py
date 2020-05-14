from django.urls import path, include
from  .views import MemorialListView, MemorialDetailView



urlpatterns = [ 
        path('<int:pk>', MemorialDetailView.as_view(), name='memorial'),
        path('', MemorialListView.as_view(), name='list')
        ]

