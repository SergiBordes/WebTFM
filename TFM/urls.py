from django.urls import path
from . import views

'app/model_viewtype'
'TFM/TFM_detail.html'

urlpatterns = [
    path('', views.RecetaListView.as_view(), name='TFM-home'),
    path('receta/<int:pk>', views.RecetaDetailView.as_view(), name='TFM-detail'),
    path('receta/create/', views.RecetaCreateView.as_view(), name='TFM-crear'),
    path('receta/<int:pk>/update', views.RecetaUpdateView.as_view(), name='TFM-update'),
    path('receta/<int:pk>/delete', views.RecetaDeleteView.as_view(), name='TFM-delete'),
    path('about/', views.about, name='TFM-about'),
    path('index/', views.index, name='TFM-index'),
]
