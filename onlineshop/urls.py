"""onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from onlineshopapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home' ),
    path('about/', views.AboutView.as_view(), name='about' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail' ),
    path('cart/added/<int:id>', views.AddedToCartView.as_view(), name='cart-added'),
    path('cart/', views.ShoppingCartView.as_view(), name='cart'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 127.0.0.1/admin/
# 127.0.0.1/
# 127.0.0.1/about/