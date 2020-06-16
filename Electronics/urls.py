from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("details/<str:item>/<str:id>", views.detail, name="detail"),
    path("buy/<str:item>/<str:name>", views.buy, name="buy"),
    path("login", views.loginhandle, name="loginhandle"),
    path("signup", views.signinhandle, name="signinhandle"), 
    path("logout", views.logoutnhandle, name="logoutnhandle"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("my_cart", views.my_cart ,name="my_cart"),
    path("remove/<str:id>", views.remove, name="remove"),
    path("handlerequest", views.handlerequest, name="handlerequest"),
    path("order", views.order, name="order"),
    path("order/my_cart", views.my_cart_order, name="my_cart_order"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
