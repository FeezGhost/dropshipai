from django.contrib import admin
from django.urls import path, include
from usersapp import views
from rest_framework_nested import routers
from productapp import views as productViews

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('product/ping/', productViews.ping, name="product_ping"),
    path('product/', productViews.getRandomProduct, name="product"),
]
