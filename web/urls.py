"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home.views import index
from accounts import urls as urls_accounts
from cart import urls as urls_cart

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('products.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('', index, name='index'),
                  path('cart/', include('cart.urls')),
                  path('checkout/', include('checkout.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
