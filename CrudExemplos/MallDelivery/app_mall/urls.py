from django.urls import path 

from app_mall import views 



urlpatterns = [ 
    path('cadastro_lojista/', views.LojistaCreateView.as_view(), name='cadastro_lojista'),
    path('cadastro_loja/', views.LojaCreateView.as_view(), name='cadastro_loja'),
    path('add_produto/', views.ProdutoCreateView.as_view(), name='add_produto'),
    path('lista_lojista/', views.LojistaList.as_view(), name='lista_lojista'),
    path('lista_loja/', views.LojaList.as_view(), name='lista_loja'),
    path('produto/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='deletar_produto'),
    path('lojista/<int:pk>/deletar/', views.LojistaDeleteView.as_view(), name='deletar_lojista'),
    path('loja/<int:pk>/deletar/', views.LojaDeleteView.as_view(), name='deletar_loja'),
    path('produto/<pk>/update/', views.ProdutoUpdateView.as_view(), name='update_produto'),
    path('lojista/<pk>/update/', views.LojistaUpdateView.as_view(), name='update_lojista'),
    path('loja/<pk>/update/', views.LojaUpdateView.as_view(), name='update_loja'),
    path('', views.ProdutoList.as_view(), name='index'), 
] 