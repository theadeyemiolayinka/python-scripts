from django.contrib import admin
from django.urls import path
from url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<slug:short_url>', views.shorten, name='shorten'),
]
