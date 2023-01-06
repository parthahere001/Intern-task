from django.urls import path
from dash import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('filterpage/', views.filterpage, name='filterpage'),
    path('filterpage/filterdata/', views.filterdata, name='filterdata'),
    path('filterpage/filterdataq/', views.filterdataq, name='filterdataq'),
    path('filterpage/filteroptions/', views.filteroptions, name='filteroptions'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
