"""case05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('cadastro_de_tarefas/', views.cadastro_de_tarefas, name='cadastro_de_tarefas'),
    path('cadastro_de_usuários/', views.cadastro_de_usuarios, name='cadastro_de_usuários'),
    path('Listagem_de_tarefas/', views.Listagem_de_tarefas, name='Listagem_de_tarefas')

]
