from django.urls import path, include
from .views import *

urlpatterns = [ 
        path('list', MemorialListView.as_view(), name='memorial_list'),
        path('<int:pk>/detail', MemorialDetailView.as_view(), name='memorial_detail'),
        path('<int:pk>/update', MemorialUpdateView.as_view(), name='memorial_update'),
        path('<int:pk>/delete', MemorialDeleteView.as_view(), name='memorial_delete'),
        path('new', MemorialCreateView.as_view(), name='memorial_new'),
        # Upload images
        path('<int:memorial_pk>/images_upload', UploadImageView.as_view(), name='image_upload'),
        # relation 
        path('<int:memorial_pk>/create_relation/', CreateRelationView.as_view(), name="Create_realtion"),
        ]

