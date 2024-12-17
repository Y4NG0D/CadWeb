from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista/', views.categoria, name="lista"),
    path('categoria/forms/', views.formsCat, name='formsCat'),
    path('editarCat/<int:id>', views.editarCat, name='editarCat'),
    path('categoria/detalheCat/<int:id>/', views.detalheCat, name='detalheCat'),
    path('deletarCat/<int:id>/', views.deletarCat, name='deletarCat'),
]   