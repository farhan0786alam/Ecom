from django.contrib import admin
from django.urls import path,include

from .import views

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', views.RegistrationViewSet)

urlpatterns = [
    path("",views.index,name="home"),
    path("signup",views.sign_up,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("cart",views.cart_detail,name="cart"),
    path("checkout",views.checkout,name="checkout"),
    path("order",views.order_detail,name="order"),
    path('restapi/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
