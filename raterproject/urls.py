from django.conf.urls import include
from django.urls import path
from raterprojectapi.views import register_user, login_user, GameView
from rest_framework import routers
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
