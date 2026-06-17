from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoDetailView


urlpatterns = [
    path('', ProdutoListView.as_view(), name='listar_produtos'),
    path('cadastrar/', ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='detalhes_produto'),
]