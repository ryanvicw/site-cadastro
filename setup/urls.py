
from django.contrib import admin
from django.urls import path,include
from cadastro import views
urlpatterns = [
path('',views.inicio,name='inicio'),
path('usuarios/',views.usuarios,name='listagem_usuarios'),
    # path('admin/', admin.site.urls),
    #  path('',include('cadastro.urls'))
]





