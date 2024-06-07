from django.urls import path 

from app_mall import views 



urlpatterns = [ 
    path('cadastro_lojista/', views.LojistaCreateView.as_view(), name='cadastro_lojista'),
    path('cadastro_loja/', views.LojaCreateView.as_view(), name='cadastro_loja'),
    path('add_produto/', views.ProdutoCreateView.as_view(), name='add_produto'),
    path('lista_lojista/', views.LojistaList.as_view(), name='lista_lojista'),
    path('lista_loja/', views.LojaList.as_view(), name='lista_loja'),
    path('produto/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='deletar_produto'),
    path('produto/<pk>/update/', views.ProdutoUpdateView.as_view(), name='update_produto'),
    path('', views.ProdutoList.as_view(), name='index'), 
] 