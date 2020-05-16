from django.urls import path, include



urlpatterns = [ 
        path('<int:pk>', MemorialDetailView.as_view(), name='detail'),
        path('list', MemorialListView.as_view(), name='memorial_list'),
        ]

