from django.urls import path 

from app_mall import views 



urlpatterns = [ 
    path('cadastro_lojista/', views.LojistaCreateView.as_view(), name='cadastro_lojista'),
    path("", views.ProdutoList.as_view(), name="index"), 
] 